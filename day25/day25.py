import itertools


def read_input(input=None):
    if not input:
        with open("day25/input.txt", "r") as f:
            input = f.read()
    key_locks_str = [l.strip().split("\n") for l in input.strip().split("\n\n")]

    locks = []
    keys = []
    for item in key_locks_str:
        heights = [len([1 for y in range(1, 6) if item[y][x] == "#"]) for x in range(5)]
        if item[0][0] == "#":
            locks.append(heights)
        else:
            keys.append(heights)

    return locks, keys


def part1(locks, keys):
    valid_combinations_count = 0
    for lock, key in itertools.product(locks, keys):
        if all(lock[i] + key[i] <= 5 for i in range(5)):
            valid_combinations_count += 1
    return valid_combinations_count


def main():
    locks, keys = read_input()

    ans1 = part1(locks, keys)
    print(f"{ans1=}")


if __name__ == "__main__":
    main()
