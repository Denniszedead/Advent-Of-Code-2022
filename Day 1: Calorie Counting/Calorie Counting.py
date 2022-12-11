import sys

elves_calories = []
input_file = sys.argv[1]


def collate_calories():
    with open(input_file, 'r') as fd:
        total = None
        for line in fd:
            x = line.rstrip()
            # x will be blank if it is a blank space, thus moving on to the next elf
            if x:
                if total:
                    total += int(x)
                else:
                    total = int(x)
            else:
                elves_calories.append(total)
                total = None
        if total:
            elves_calories.append(total)
    elves_calories.sort(reverse=True)


def find_sum_top_3(top_3):
    total_sum = None
    for x in top_3:
        if total_sum:
            total_sum += x
        else:
            total_sum = x
    return total_sum


if __name__ == "__main__":
    collate_calories()
    # Top calorie
    print(elves_calories[0])
    # Top 3 calories
    print(find_sum_top_3(elves_calories[:3]))
