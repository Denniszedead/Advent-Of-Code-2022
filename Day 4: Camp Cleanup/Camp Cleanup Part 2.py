import sys

input_file = sys.argv[1]


def get_range(number):
    limits = number.split("-")
    lower_limit = int(limits[0])
    upper_limit = int(limits[1])

    return [lower_limit, upper_limit]


def check_overlapping_pairs(first_member, second_member):
    if second_member[1] >= first_member[0] >= second_member[0]:
        return True
    elif second_member[0] <= first_member[1] <= second_member[1]:
        return True
    elif first_member[0] >= second_member[0] and first_member[1] <= second_member[1]:
        return True
    elif first_member[0] <= second_member[0] and first_member[1] >= second_member[1]:
        return True
    else:
        return False


if __name__ == '__main__':
    overlapping_pairs = 0

    with open(input_file, 'r') as fd:
        line = fd.readline()

        while line:
            content = line.rstrip('\n')
            areas = content.split(',')
            first_member = get_range(areas[0])
            second_member = get_range(areas[1])

            if check_overlapping_pairs(first_member, second_member):
                overlapping_pairs += 1

            line = fd.readline()

    print(overlapping_pairs)
