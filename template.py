def read_input(input=None):
    if not input:
        with open("day00/input.txt", "r") as f:
            input = f.read().strip()
        input = [l.strip() for l in input.split("\n")]
    return input


def part1(input):
    pass


def part2(input):
    pass


def main():
    test_input = """
""".strip()

    # input = read_input(test_input)
    input = read_input()

    ans1 = part1(input)
    print(f"{ans1=}")

    ans2 = part2(input)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
