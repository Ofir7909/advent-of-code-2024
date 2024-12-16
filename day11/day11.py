from functools import wraps


def read_input():
    with open("day11/input.txt", "r") as f:
        input = [int(num) for num in f.read().strip().split()]
    return input


def part1(stones: list):
    for k in range(25):
        new_stones = []
        for val in stones:
            if val == 0:
                new_stones.append(1)
            elif len(str(val)) % 2 == 0:
                val_str = str(val)
                n = len(val_str) // 2
                new_stones.append(int(val_str[:n]))
                new_stones.append(int(val_str[n:]))
            else:
                new_stones.append(val * 2024)
        stones = new_stones
    return len(stones)


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def stones_count_rec(val: int, steps: int):
    if steps == 0:
        return 1

    if val == 0:
        return stones_count_rec(1, steps - 1)
    elif len(str(val)) % 2 == 0:
        val_str = str(val)
        n = len(val_str) // 2
        return stones_count_rec(int(val_str[:n]), steps - 1) + stones_count_rec(
            int(val_str[n:]), steps - 1
        )
    else:
        return stones_count_rec(val * 2024, steps - 1)


def part2(stones):
    stones_count = 0
    for stone in stones:
        stones_count += stones_count_rec(stone, 75)
    return stones_count


def main():
    input = read_input()

    ans1 = part1(input.copy())
    print(f"{ans1=}")

    ans2 = part2(input.copy())
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
