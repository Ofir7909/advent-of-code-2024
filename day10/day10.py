def read_input():
    with open("day10/input.txt", "r") as f:
        input = [list(map(int, l.strip())) for l in f.readlines()]
    return input


def count_trails(input, start: tuple[int, int], endings: set):
    n = len(input)
    m = len(input[0])

    ch = input[start[0]][start[1]]

    if ch == 9:
        endings.add((start))
        return 1

    trails = 0
    if start[0] > 0 and input[start[0] - 1][start[1]] == ch + 1:
        trails += count_trails(input, (start[0] - 1, start[1]), endings)
    if start[0] < n - 1 and input[start[0] + 1][start[1]] == ch + 1:
        trails += count_trails(input, (start[0] + 1, start[1]), endings)
    if start[1] > 0 and input[start[0]][start[1] - 1] == ch + 1:
        trails += count_trails(input, (start[0], start[1] - 1), endings)
    if start[1] < m - 1 and input[start[0]][start[1] + 1] == ch + 1:
        trails += count_trails(input, (start[0], start[1] + 1), endings)
    return trails


def part1(input):
    n = len(input)
    m = len(input[0])

    sum = 0
    for i in range(n):
        for j in range(m):
            if input[i][j] != 0:
                continue
            endings = set()
            count_trails(input, (i, j), endings)
            sum += len(endings)
    return sum


def part2(input):
    n = len(input)
    m = len(input[0])

    sum = 0
    for i in range(n):
        for j in range(m):
            if input[i][j] != 0:
                continue
            endings = set()
            sum += count_trails(input, (i, j), endings)
    return sum


def main():
    input = read_input()

    ans1 = part1(input)
    print(f"{ans1=}")

    ans2 = part2(input)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
