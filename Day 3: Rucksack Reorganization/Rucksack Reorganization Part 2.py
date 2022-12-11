import sys


priority_mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                    'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                    'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34,
                    'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45,
                    'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

input = sys.argv[1]


def find_intersection(first_array, second_array):
    length_first_array = len(first_array)
    length_second_array = len(second_array)

    first_index = 0
    second_index = 0

    result = []

    while True:
        if first_index >= length_first_array or second_index >= length_second_array:
            break
        else:
            if priority_mapping[first_array[first_index]] == priority_mapping[second_array[second_index]]:
                result.append(first_array[first_index])
                first_index += 1
            elif priority_mapping[first_array[first_index]] <= priority_mapping[second_array[second_index]]:
                first_index += 1
            elif priority_mapping[first_array[first_index]] > priority_mapping[second_array[second_index]]:
                second_index += 1

    result = list(dict.fromkeys(result))
    return result


if __name__ == "__main__":
    total_priority = None

    with open(input, 'r') as fd:
        line = fd.readline()

        while line:
            first_member_line = line.rstrip('\n')
            second_member_line = fd.readline().rstrip('\n')
            third_member_line = fd.readline().rstrip('\n')

            first_member = sorted([*first_member_line], key= lambda x: priority_mapping[x])
            second_member = sorted([*second_member_line], key= lambda x: priority_mapping[x])
            third_member = sorted([*third_member_line], key= lambda x: priority_mapping[x])

            first_second_intersection = find_intersection(first_member, second_member)
            common_element = find_intersection(first_second_intersection, third_member)[0]

            if total_priority:
                total_priority += priority_mapping[common_element]
            else:
                total_priority = priority_mapping[common_element]

            line = fd.readline()

    print(total_priority)