import sys

priority_mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                    'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                    'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34,
                    'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45,
                    'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

input = sys.argv[1]


def search_common_element(first_array, second_array):
    length_first_array = len(first_array)
    length_second_array = len(second_array)

    first_index = 0
    second_index = 0

    while True:
        if first_index >= length_first_array or second_index >= length_second_array:
            return None
        else:
            if priority_mapping[first_array[first_index]] == priority_mapping[second_array[second_index]]:
                return first_array[first_index]
            elif priority_mapping[first_array[first_index]] <= priority_mapping[second_array[second_index]]:
                first_index += 1
            elif priority_mapping[first_array[first_index]] > priority_mapping[second_array[second_index]]:
                second_index += 1


if __name__ == "__main__":
    total_priority = None

    with open(input, 'r') as fd:
        line = fd.readline()
        while line:
            items_in_rucksack = line.rstrip('\n')
            length_of_items = len(items_in_rucksack)
            half_index = length_of_items // 2
            first_compartment = items_in_rucksack[:half_index]
            second_compartment = items_in_rucksack[half_index:]

            first_compartment_sorted = sorted([*first_compartment], key= lambda x: priority_mapping[x])
            second_compartment_sorted = sorted([*second_compartment], key= lambda x: priority_mapping[x])

            common = search_common_element(first_compartment_sorted, second_compartment_sorted)

            if total_priority:
                total_priority += priority_mapping[common]
            else:
                total_priority = priority_mapping[common]

            line = fd.readline()

    print(total_priority)
