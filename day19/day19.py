from functools import wraps


def read_input(input=None):
    if not input:
        with open("day19/input.txt", "r") as f:
            input = f.read().strip()
    inp1 = input.split("\n\n")[0].strip()
    inp2 = input.split("\n\n")[1].strip()

    towels = [t.strip() for t in inp1.split(",")]
    designs = [d.strip() for d in inp2.split("\n")]

    return towels, designs


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


def part1(towels, designs):
    @memoize
    def is_possible(design: str):
        if len(design) == 0:
            return True
        for t in towels:
            if design.startswith(t):
                if is_possible(design[len(t) :]):
                    return True
        return False

    possible_designs = 0
    for d in designs:
        if is_possible(d):
            possible_designs += 1

    return possible_designs


def part2(towels, designs):
    @memoize
    def num_of_possible_ways(design: str):
        if len(design) == 0:
            return 1

        count = 0
        for t in towels:
            if design.startswith(t):
                count += num_of_possible_ways(design[len(t) :])
        return count

    possible_designs = 0
    for d in designs:
        possible_designs += num_of_possible_ways(d)

    return possible_designs


def main():
    test_input = """
""".strip()

    # input = read_input(test_input)
    towels, designs = read_input()

    ans1 = part1(towels, designs)
    print(f"{ans1=}")

    ans2 = part2(towels, designs)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
