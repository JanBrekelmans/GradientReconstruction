import numpy as np

def read_unv_mesh(file_location: str):
    nodes = None
    elements = None
    with open(file_location, "r") as reader:
        for line in reader:
            stripped_line = line.strip()
            if stripped_line == "-1":
                continue
            elif stripped_line == "2411":
                nodes = read_unv_nodes(reader)
            elif stripped_line == "2412":
                elements = read_unv_elements(reader)
    return [np.asarray(nodes), np.asarray(elements)]

def read_unv_mesh_as_2d(file_location: str):
    [nodes_3d, elements] = read_unv_mesh(file_location)

    return [nodes_3d[:,:-1], elements]


def read_unv_nodes(reader) -> list[list[float]]:
    nodes = []

    line = reader.readline()
    while line != '':
        stripped_line = line.strip()
        if "-1" in stripped_line:
            return nodes
        else:
            next_line = reader.readline()
            stripped_line = next_line.strip()
            new_node = [float(s) for s in stripped_line.split()]
            nodes.append(new_node)
        line = reader.readline()

def read_unv_elements(reader):
    elements = []

    line = reader.readline()
    while line != '':
        stripped_line = line.strip()
        if "-1" in stripped_line:
            return elements
        else:
            splitted_line = stripped_line.split()
            feId = int(splitted_line[1])
            if feId == 11:
                # Rod -> skip
                reader.readline()
                reader.readline()
            elif feId == 41 or feId == 44:
                # Triangle/Quad
                nodeLine = reader.readline()
                splitted_node_line = nodeLine.split()
                elements.append([int(s)-1 for s in splitted_node_line])

        line = reader.readline()

