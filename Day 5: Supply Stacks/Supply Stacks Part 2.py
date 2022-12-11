import sys

import Schematic_9001 as Schematic

input_file = sys.argv[1]


def create_schematic(schematic_array):
    return schematic_array


if __name__ == '__main__':
    with open(input_file, 'r') as fd:
        lines = fd.readlines()

        index_of_moves = lines.index('\n')

        schematic = Schematic.Schematic(lines[:index_of_moves])
        list_of_moves = list(map(lambda x: x.rstrip('\n'), lines[index_of_moves+1:]))

        for move in list_of_moves:
            schematic.move_crate(move)

print(schematic.schematic)
