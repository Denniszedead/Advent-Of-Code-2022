import sys
import Shape

input = sys.argv[1]

if __name__ == "__main__":
    total_points = None

    with open(input, 'r') as fd:
        line = fd.readline()
        while line:
            content = line.rstrip('\n').split(' ')
            opponent_shape = Shape.opponent_shape(content[0])
            player_shape = Shape.player_shape(content[1])
            points = player_shape.play(opponent_shape)

            if total_points:
                total_points += points
            else:
                total_points = points

            line = fd.readline()

    print(total_points)
