def read_input():
    with open("day12/input.txt", "r") as f:
        input = [l.strip() for l in f.readlines()]
    return input


def calc_area(input, start, plot: set):
    if start in plot:
        return 0
    plot.add(start)

    n = len(input)
    m = len(input[0])

    ch = input[start[0]][start[1]]

    area = 1
    if start[0] > 0 and input[start[0] - 1][start[1]] == ch:
        area += calc_area(input, (start[0] - 1, start[1]), plot)
    if start[0] < n - 1 and input[start[0] + 1][start[1]] == ch:
        area += calc_area(input, (start[0] + 1, start[1]), plot)
    if start[1] > 0 and input[start[0]][start[1] - 1] == ch:
        area += calc_area(input, (start[0], start[1] - 1), plot)
    if start[1] < m - 1 and input[start[0]][start[1] + 1] == ch:
        area += calc_area(input, (start[0], start[1] + 1), plot)
    return area


def calc_perm(plot):
    perm = len(plot) * 4
    for r in plot:
        if (r[0] + 1, r[1]) in plot:
            perm -= 2
        if (r[0], r[1] + 1) in plot:
            perm -= 2
    return perm


def part1(input):
    n = len(input)
    m = len(input[0])

    seen = set()

    answer = 0
    for i in range(n):
        for j in range(m):
            if (i, j) in seen:
                continue

            plot = set()
            area = calc_area(input, (i, j), plot)
            perm = calc_perm(plot)
            seen = seen.union(plot)
            answer += area * perm
    return answer


def count_sides(plot):
    sides = calc_perm(plot)

    for r in plot:
        if (r[0] + 1, r[1]) not in plot:
            if (r[0], r[1] + 1) in plot and (r[0] + 1, r[1] + 1) not in plot:
                sides -= 1
        if (r[0], r[1] + 1) not in plot:
            if (r[0] + 1, r[1]) in plot and (r[0] + 1, r[1] + 1) not in plot:
                sides -= 1
        if (r[0] - 1, r[1]) not in plot:
            if (r[0], r[1] - 1) in plot and (r[0] - 1, r[1] - 1) not in plot:
                sides -= 1
        if (r[0], r[1] - 1) not in plot:
            if (r[0] - 1, r[1]) in plot and (r[0] - 1, r[1] - 1) not in plot:
                sides -= 1
    return sides


def part2(input):
    n = len(input)
    m = len(input[0])

    seen = set()

    answer = 0
    for i in range(n):
        for j in range(m):
            if (i, j) in seen:
                continue

            plot = set()
            area = calc_area(input, (i, j), plot)
            sides = count_sides(plot)
            seen = seen.union(plot)
            answer += area * sides
    return answer


def main():
    input = read_input()

    ans1 = part1(input)
    print(f"{ans1=}")

    ans2 = part2(input)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
