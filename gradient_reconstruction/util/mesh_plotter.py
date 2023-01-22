import matplotlib.pyplot as plt


def plot_mesh(nodes, elements):
    for element in elements:
        x = [nodes[e][0] for e in element]
        y = [nodes[e][1] for e in element]
        plt.fill(x, y, edgecolor='black', fill=False)


def plot_points(points, format="o", color="black"):
    plt.plot(points[:, 0], points[:, 1], format, color=color)


def elements_to_triangles(elements):
    triangles = []

    for i, element in iter(elements):
        if len(element) == 3:
            triangles.append(element)
        elif len(element) == 4:
            triangle1 = [element[i] for i in range(3)]
            triangle2 = [element[i] for i in range(1, 4)]
            triangles.append(triangle1)
            triangles.append(triangle2)
        else:
            raise Exception("Only triangles and quads are supported")
    return triangles
