from typing import Callable
from dataclasses import dataclass


class Monkey:
    id: int
    items: list[int]
    inspect: Callable[[int], int]
    divisible: int
    test: Callable[[int], bool]
    decide: Callable[[bool], int]
    total_inspects = 0

    def __init__(self, id, items, inspect, divisible, decide) -> None:
        self.id = id
        self.items = items
        self.inspect = inspect
        self.test = lambda item: item % divisible == 0
        self.divisible = divisible
        self.decide = decide


@dataclass
class KeepAway:
    total_rounds: int
    monkeys: list[Monkey]
    modules: int = 1

    def round(self):
        for monkey in self.monkeys:
            for item in monkey.items.copy():
                current_worry_level = monkey.inspect(item)
                monkey.total_inspects += 1
                result = monkey.test(current_worry_level)
                receiving_monkey = monkey.decide(result)
                current_worry_level = current_worry_level % self.modules
                self.monkeys[receiving_monkey].items.append(current_worry_level)
                monkey.items.remove(item)

    def start(self):
        for monkey in self.monkeys:
            self.modules *= monkey.divisible

        for r in range(self.total_rounds):
            self.round()
            print(f"{r} rounds completed")


monkeys: list[Monkey] = []
monkeys.append(
    Monkey(
        0,
        [72, 97],
        lambda old: old * 13,
        19,
        lambda result: 5 if result else 6,
    )
)
monkeys.append(
    Monkey(
        1,
        [55, 70, 90, 74, 95],
        lambda old: old * old,
        7,
        lambda result: 5 if result else 0,
    )
)
monkeys.append(
    Monkey(
        2,
        [74, 97, 66, 57],
        lambda old: old + 6,
        17,
        lambda result: 1 if result else 0,
    )
)
monkeys.append(
    Monkey(
        3,
        [86, 54, 53],
        lambda old: old + 2,
        13,
        lambda result: 1 if result else 2,
    )
)
monkeys.append(
    Monkey(
        4,
        [50, 65, 78, 50, 62, 99],
        lambda old: old + 3,
        11,
        lambda result: 3 if result else 7,
    )
)
monkeys.append(
    Monkey(
        5,
        [90],
        lambda old: old + 4,
        2,
        lambda result: 4 if result else 6,
    )
)
monkeys.append(
    Monkey(
        6,
        [88, 92, 63, 94, 96, 82, 53, 53],
        lambda old: old + 8,
        5,
        lambda result: 4 if result else 7,
    )
)
monkeys.append(
    Monkey(
        7,
        [70, 60, 71, 69, 77, 70, 98],
        lambda old: old * 7,
        3,
        lambda result: 2 if result else 3,
    )
)


game = KeepAway(10000, monkeys)
game.start()
monkeys.sort(key=lambda monkey: monkey.total_inspects, reverse=True)
highest = monkeys[:2]
monkey_business = highest[0].total_inspects * highest[1].total_inspects

print(monkey_business)
