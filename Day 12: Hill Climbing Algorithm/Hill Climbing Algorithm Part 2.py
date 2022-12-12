import math
import sys

input_file = sys.argv[1]


def cord_to_str(coordinates):
    return f'{coordinates}'


def build_adjacency_list(grid):
    adjacency_list = {}
    coordinates_with_a = []

    for row_no in range(len(grid)):
        for col_no in range(len(grid[row_no])):
            elevation = grid[row_no][col_no]
            curr_coordinates = (row_no, col_no)
            if elevation == 'S':
                elevation = 'a'
            elif elevation == 'E':
                elevation = 'z'
                destination = (row_no, col_no)
            selected_node = cord_to_str(curr_coordinates)
            if elevation == 'a':
                coordinates_with_a.append(selected_node)
            adjacency_list[selected_node] = find_neighbours(grid, elevation, row_no, col_no)

    return cord_to_str(destination), coordinates_with_a, adjacency_list


def is_neighbour(source, destination):
    ascii_source = ord(source)
    if destination == 'E':
        ascii_destination = ord('z')
    elif destination == 'S':
        ascii_destination = ord('a')
    else:
        ascii_destination = ord(destination)
    if ascii_source >= ascii_destination:
        return True
    else:
        return ascii_destination - ascii_source == 1


def find_neighbours(grid, cur_elevation, row_no, col_no):
    neighbours = []
    if row_no < (len(grid) - 1):
        neighbour_row_no = row_no + 1
        neighbour_elevation = grid[neighbour_row_no][col_no]
        neighbour_coordinates = (neighbour_row_no, col_no)
        if is_neighbour(cur_elevation, neighbour_elevation):
            neighbours.append(cord_to_str(neighbour_coordinates))
    if row_no > 0:
        neighbour_row_no = row_no - 1
        neighbour_elevation = grid[neighbour_row_no][col_no]
        neighbour_coordinates = (neighbour_row_no, col_no)
        if is_neighbour(cur_elevation, neighbour_elevation):
            neighbours.append(cord_to_str(neighbour_coordinates))
    if col_no < (len(grid[row_no]) - 1):
        neighbour_col_no = col_no + 1
        neighbour_elevation = grid[row_no][neighbour_col_no]
        neighbour_coordinates = (row_no, neighbour_col_no)
        if is_neighbour(cur_elevation, neighbour_elevation):
            neighbours.append(cord_to_str(neighbour_coordinates))
    if col_no > 0:
        neighbour_col_no = col_no - 1
        neighbour_elevation = grid[row_no][neighbour_col_no]
        neighbour_coordinates = (row_no, neighbour_col_no)
        if is_neighbour(cur_elevation, neighbour_elevation):
            neighbours.append(cord_to_str(neighbour_coordinates))

    return neighbours


def modified_bfs_algorithm(adjacency_list, source, destination):
    no_steps = {}
    path = {}
    queue = [source]

    for coordinate in adjacency_list.keys():
        no_steps[coordinate] = None
        path[coordinate] = None

    no_steps[source] = 0

    while len(queue) > 0:
        selected_node = queue.pop(0)

        for neighbour in adjacency_list[selected_node]:
            if no_steps[neighbour] is None:
                no_steps[neighbour] = no_steps[selected_node] + 1
                path[neighbour] = selected_node
                queue.append(neighbour)

    return no_steps, path


if __name__ == '__main__':
    with open(input_file, 'r') as fd:
        grid = list(map(lambda line: list(line.rstrip('\n')), fd.readlines()))
        destination, coordinates_with_a, adjacency_list = build_adjacency_list(grid)

        lowest_steps = math.inf

        for source_coordinates in coordinates_with_a:
           steps, path = modified_bfs_algorithm(adjacency_list, source_coordinates, destination)
           no_steps = steps[destination]
           if no_steps and lowest_steps > no_steps:
               lowest_steps = no_steps

        print(lowest_steps)
