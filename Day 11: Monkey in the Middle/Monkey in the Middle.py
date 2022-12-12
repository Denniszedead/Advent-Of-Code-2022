import math
from math import lcm

from Monkey import Monkey, all_monkeys_throw_items_part_1, all_monkeys_throw_items_part_2

if __name__ == '__main__':
    # Manually add monkey based on the Moneky class
    monkeys = []

    modulo = lcm(*[monkey.divisible_by for monkey in monkeys])

    for x in range(10000):
        #change to all_monkeys_throw_items_part_1 when using part 1
        all_monkeys_throw_items_part_2(monkeys, modulo)

    monkey_businesses = []

    for monkey in monkeys:
        monkey_businesses.append(monkey.monkey_business)

    sorted_monkey_business = sorted(monkey_businesses, reverse=True)

    print(sorted_monkey_business[0] * sorted_monkey_business[1])
