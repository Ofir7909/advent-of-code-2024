import itertools
def read_input():
    with open("day07/input.txt", "r") as f:
        input = [l.strip() for l in f.readlines()]
    return input


def part1(input):
    answer = 0
    for l in input:
        test_value = int(l.split(":")[0])
        values = list(map(int,l.split(":")[1].split()))

        for operations in range(2**(len(values)-1)):
            mask = 0b1
            result = values[0]
            for val in values[1:]:
                if operations & mask == 0:
                    result += val
                else:
                    result *= val
                mask = mask << 1

            if result == test_value:
                answer += test_value
                break
    return answer


def part2(input):
    answer = 0
    for l in input:
        test_value = int(l.split(":")[0])
        values = list(map(int,l.split(":")[1].split()))

        for operations in itertools.product(range(3), repeat=len(values)-1):
            result = values[0]
            for i, val in enumerate(values[1:]):
                if operations[i] == 0:
                    result += val
                elif operations[i] == 1:
                    result *= val
                else:
                    digits = len(str(val))
                    result = result * 10**digits + val

            if result == test_value:
                answer += test_value
                break
    return answer


def main():
    input = read_input()

    ans1 = part1(input)
    print(f"{ans1=}")

    ans2 = part2(input)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
