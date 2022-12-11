def all_monkeys_throw_items_part_1(monkeys):
    for monkey in monkeys:
        monkey.throw_item_part_1(monkeys)


def all_monkeys_throw_items_part_2(monkeys, modulo):
    for monkey in monkeys:
        monkey.throw_item_part_2(monkeys, modulo)


class Monkey:
    def __init__(self, worry_levels, operation, divisible_by, throw_if_true, throw_if_false):
        self.worry_levels = worry_levels
        self.operation = operation
        self.divisible_by = divisible_by
        self.throw_if_true = throw_if_true
        self.throw_if_false = throw_if_false
        self.monkey_business = 0

    def throw_item_part_1(self, monkeys):
        while len(self.worry_levels) > 0:
            worry_level = self.worry_levels.pop(0)
            # Monkey inspect item
            worry_level_after_inspection = self.operation(worry_level)
            decreased_worry_level = worry_level_after_inspection // 3
            # Monkey throw item
            recipient_monkey = self.throw_if_true \
                if decreased_worry_level % self.divisible_by == 0 else self.throw_if_false
            monkeys[recipient_monkey].receive_item(decreased_worry_level)
            self.monkey_business += 1

    def throw_item_part_2(self, monkeys, modulo):
        while len(self.worry_levels) > 0:
            worry_level = self.worry_levels.pop(0)
            # Monkey inspect item
            worry_level_after_inspection = self.operation(worry_level) % modulo
            # Monkey throw item
            recipient_monkey = self.throw_if_true \
                if worry_level_after_inspection % self.divisible_by == 0 else self.throw_if_false
            monkeys[recipient_monkey].receive_item(worry_level_after_inspection)
            self.monkey_business += 1

    def receive_item(self, new_worry_level):
        self.worry_levels.append(new_worry_level)
