from dataclasses import dataclass
import itertools


def read_input(input=None):
    if not input:
        with open("day22/input.txt", "r") as f:
            input = f.read()
    input = [int(l.strip()) for l in input.strip().split("\n")]
    return input


def mix(secret, new_secret):
    return secret ^ new_secret


def prune(secret):
    return secret % 16777216


def get_secret_number(secret, n):
    for i in range(n):
        secret = prune(mix(secret, secret << 6))
        secret = prune(mix(secret, secret >> 5))
        secret = prune(mix(secret, secret << 11))
    return secret


def part1(input):
    return sum(get_secret_number(num, 2000) for num in input)


def get_all_prices(secret, n):
    prices = []
    prices.append(secret % 10)

    for i in range(n):
        secret = prune(mix(secret, secret << 6))
        secret = prune(mix(secret, secret >> 5))
        secret = prune(mix(secret, secret << 11))
        prices.append(secret % 10)
    return prices


def part2(input):
    @dataclass
    class Monkey:
        prices: list[int]
        changes: str

    change_to_char = {
        -9: "i",
        -8: "h",
        -7: "g",
        -6: "f",
        -5: "e",
        -4: "d",
        -3: "c",
        -2: "b",
        -1: "a",
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
    }
    char_to_change = {v: k for k, v in change_to_char.items()}

    n = 2000
    monkeys: list[Monkey] = []
    for num in input:
        prices = get_all_prices(num, n)
        changes = "".join(change_to_char[b - a] for a, b in zip(prices, prices[1:]))
        monkeys.append(Monkey(prices, changes))

    max_bananas = 0
    for seq in itertools.product("ihgfedcba0123456789", repeat=4):
        # skip impossible sequences
        is_possible = True
        for length in range(2, 5):
            for start in range(5 - length):
                seq_sum = sum(char_to_change[c] for c in seq[start : start + length])
                if not (-8 <= seq_sum <= 9):
                    is_possible = False

        if not is_possible:
            continue

        seq_str = "".join(seq)
        total_bananas = 0
        # print(seq_str, max_bananas)
        for m in monkeys:
            index = m.changes.find(seq_str)
            if index == -1:
                continue
            total_bananas += m.prices[index + 4]
        max_bananas = max(max_bananas, total_bananas)

    return max_bananas


def main():
    test_input = """
1
2
3
2024
"""

    # input = read_input(test_input)
    input = read_input()

    ans1 = part1(input)
    print(f"{ans1=}")

    ans2 = part2(input)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
