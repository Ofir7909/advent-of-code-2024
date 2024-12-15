def read_input():
    with open("day00/input.txt", "r") as f:
        input = [l.strip() for l in f.readlines()]
    return input


def part1(input):
    pass


def part2(input):
    pass


def main():
    input = read_input()

    ans1 = part1(input)
    print(f"{ans1=}")

    ans2 = part2(input)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
