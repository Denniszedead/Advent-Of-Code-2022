import sys

input_file = sys.argv[1]


def get_lower_and_upper_limits(number):
    limits = number.split("-")
    lower_limit = int(limits[0])
    upper_limit = int(limits[1])

    return [lower_limit, upper_limit]


def check_containing_pairs(first_limits, second_limits):
    if first_limits[0] >= second_limits[0] and first_limits[1] <= second_limits[1]:
        return True
    elif first_limits[0] <= second_limits[0] and first_limits[1] >= second_limits[1]:
        return True
    else:
        return False


if __name__ == '__main__':
    fully_containing_pairs = 0

    with open(input_file, 'r') as fd:
        line = fd.readline()

        while line:
            content = line.rstrip('\n')
            areas = content.split(',')
            first_member = get_lower_and_upper_limits(areas[0])
            second_member = get_lower_and_upper_limits(areas[1])

            if check_containing_pairs(first_member, second_member):
                fully_containing_pairs += 1

            line = fd.readline()

    print(fully_containing_pairs)