import numpy as np

_PRECISION = 1e-4


def compute_cell_midpoints(nodes, elements):
    mid_points = np.zeros((elements.shape[0], 2))

    for i, element in enumerate(elements):
        mid_points[i, :] = np.sum(nodes[element], axis=0) / element.size

    return mid_points


def _compute_area_of_triangle(t1, t2, t3):
    t21 = t2 - t1
    t31 = t3 - t1

    area_vec = t21[0] * t31[1] - t21[1] * t31[0]

    return 0.5 * np.abs(area_vec)


def compute_cell_centroids(nodes, elements):
    centroids = compute_cell_midpoints(nodes, elements)

    for i, element in enumerate(elements):
        centroid = centroids[i]
        old_centroid = centroid + 1  # Set first step wrong

        while np.max(np.abs(centroid - old_centroid)) > _PRECISION:
            total_area = 0
            old_centroid = centroid
            centroid = np.zeros(2)

            for node_index in range(element.size):
                node_vec = nodes[element[node_index]]
                next_node_vec = nodes[element[(node_index + 1) % element.size]]

                triangle_area = _compute_area_of_triangle(old_centroid, node_vec, next_node_vec)
                total_area += triangle_area

                centroid += triangle_area * (old_centroid + node_vec + next_node_vec) / 3.0

            centroid /= total_area

        centroids[i] = centroid

    return centroids


def create_node_to_element_information(elements):
    max_node_index = 0
    for element in elements:
        max_node_index = max(max_node_index, max(element))

    node_information = [[] for _ in range(max_node_index + 1)]

    for i, element in enumerate(elements):
        for node_index in element:
            node_information[node_index].append(i)

    return node_information


def create_face_information(elements):
    faces_to_cells_map = dict()
    face_to_points_map = dict()

    new_face_index = 0

    for element_index, element in enumerate(elements):
        for i in range(element):
            point_index1 = element[i]
            point_index2 = element[(i + 1) % len(element)]

            face = [point_index1, point_index2]

            if not face in face_to_points_map.keys():
                face_to_points_map[face] = new_face_index
                faces_to_cells_map[new_face_index] = [-1, -1]
                new_face_index += 1

            face_cells = faces_to_cells_map[face]

            if face_cells[0] == -1:
                face_cells[0] = element_index
            else:
                face_cells[1] = element_index

            faces_to_cells_map[face] = face_cells

    return face_to_points_map, faces_to_cells_map
