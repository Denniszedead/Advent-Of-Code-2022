import sys

input_file = sys.argv[1]

X = 1
cycle_no = 0
signal_strength = 0


def add_signal(V):
    global X
    X += V


def add_signal_strength():
    global signal_strength
    if cycle_no == 20 or cycle_no == 60 or cycle_no == 100 or cycle_no == 140 or cycle_no == 180 or cycle_no == 220:
        current_signal_strength = cycle_no * X
        print(f'Signal strength at {cycle_no}: {current_signal_strength}')
        signal_strength += current_signal_strength


if __name__ == "__main__":
    with open(input_file, 'r') as fd:
        lines = fd.readlines()
        instructions = list(map(lambda line: line.rstrip('\n').split(' '), lines))

        for instruction in instructions:
            if instruction[0] == 'addx':
                for increment in range(2):
                    cycle_no += 1
                    add_signal_strength()
                add_signal(int(instruction[1]))
            elif instruction[0] == 'noop':
                cycle_no += 1
                add_signal_strength()

    print(signal_strength)
