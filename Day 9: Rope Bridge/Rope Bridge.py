import sys
from RopePositionPartOne import RopePositionPartOne
from RopePositionPartTwo import RopePositionPartTwo

input_file = sys.argv[1]

if __name__ == '__main__':
    with open(input_file, 'r') as fd:
        movements = list(map(lambda line: line.rstrip('\n').split(' '), fd.readlines()))
        ropePositionPart1 = RopePositionPartOne()
        ropePositionPart2 = RopePositionPartTwo()

        for movement in movements:
            ropePositionPart1.move_rope(movement)
            ropePositionPart2.move_rope(movement)

        print(len(ropePositionPart1.get_tail_visited()))

        print(len(ropePositionPart2.get_tail_visited()))
