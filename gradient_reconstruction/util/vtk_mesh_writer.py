def _create_vtk_header(title="Data"):
    return '# vtk DataFile Version 2.0\n' \
           + title + '\n' \
           + 'ASCII\n\n'


def _create_vtk_data_set(nodes, elements):
    dataset_text = 'DATASET UNSTRUCTURED_GRID\n' \
                   + 'POINTS ' + str(nodes.size) + ' float\n'

    for node in nodes:
        dataset_text += str(node[0]) + '\t' + str(node[1]) + '\t' + '0.0' + '\n'

    dataset_text += '\n'

    dataset_text += 'CELLS ' + str(elements.shape[0]) + ' ' + str(elements.size + elements.shape[0]) + '\n'

    for element in elements:
        dataset_text += str(element.size)
        for e in element:
            dataset_text += ' ' + str(e)
        dataset_text += "\n"

    dataset_text += '\n'
    dataset_text += 'CELL_TYPES ' + str(elements.shape[0]) + '\n'
    for _ in elements:
        dataset_text += "7\n"

    return dataset_text


def _create_vtk_cell_data(values, name='val'):
    cell_data_text = 'CELL_DATA ' + str(len(values)) + '\n' \
                     + 'SCALARS ' + name + ' float\n' \
                     + 'LOOKUP_TABLE default\n'

    for value in values:
        cell_data_text += str(value) + '\n'

    return cell_data_text


def write_to_vtk(file_location, nodes, elements, values):
    with open(file_location, 'w') as file:
        file.write(_create_vtk_header())
        file.write(_create_vtk_data_set(nodes, elements))
        file.write(_create_vtk_cell_data(values))
