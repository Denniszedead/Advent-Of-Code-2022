import math
from math import lcm

from Monkey import Monkey, all_monkeys_throw_items_part_1, all_monkeys_throw_items_part_2

if __name__ == '__main__':
    monkeys_one = [
        Monkey([79, 98], lambda old: old * 19, 23, 2, 3),
        Monkey([54, 65, 75, 74], lambda old: old + 6, 19, 2, 0),
        Monkey([79, 60, 97], lambda old: old * old, 13, 1, 3),
        Monkey([74], lambda old:old + 3, 17, 0, 1)
    ]

    monkeys_two = [
        Monkey([72, 97], lambda old: old * 13, 19, 5, 6),
        Monkey([55, 70, 90, 74, 95], lambda old: old * old, 7, 5, 0),
        Monkey([74, 97, 66, 57], lambda old: old + 6, 17, 1, 0),
        Monkey([86, 54, 53], lambda old: old + 2, 13, 1, 2),
        Monkey([50, 65, 78, 50, 62, 99], lambda old: old + 3, 11, 3, 7),
        Monkey([90], lambda old: old + 4, 2, 4, 6),
        Monkey([88 ,92, 63, 94, 96, 82, 53, 53], lambda old: old + 8, 5, 4, 7),
        Monkey([70, 60, 71, 69, 77, 70, 98], lambda old:old * 7, 3, 2, 3)
    ]

    modulo = lcm(*[monkey.divisible_by for monkey in monkeys_two])

    for x in range(10000):
        #change to all_monkeys_throw_items_part_1 when using part 1
        all_monkeys_throw_items_part_2(monkeys_two, modulo)

    monkey_businesses = []

    for monkey in monkeys_two:
        monkey_businesses.append(monkey.monkey_business)

    sorted_monkey_business = sorted(monkey_businesses, reverse=True)

    print(sorted_monkey_business[0] * sorted_monkey_business[1])
