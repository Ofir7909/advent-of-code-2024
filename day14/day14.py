def read_input():
    with open("day14/input.txt", "r") as f:
        input = [l.strip() for l in f.readlines()]

    robots = []
    for l in input:
        p = tuple(map(int, l.split()[0].removeprefix("p=").split(",")))
        v = tuple(map(int, l.split()[1].removeprefix("v=").split(",")))
        robots.append({"p": p, "v": v})
    return robots


def add_vel(robot, w, h):
    return {
        "p": (
            (robot["p"][0] + robot["v"][0]) % w,
            (robot["p"][1] + robot["v"][1]) % h,
        ),
        "v": robot["v"],
    }


def part1(robots):
    w = 101
    h = 103

    for _ in range(100):
        robots = [add_vel(r, w, h) for r in robots]

    q1 = len([r for r in robots if r["p"][0] < w // 2 and r["p"][1] < h // 2])
    q2 = len([r for r in robots if r["p"][0] < w // 2 and r["p"][1] > h // 2])
    q3 = len([r for r in robots if r["p"][0] > w // 2 and r["p"][1] > h // 2])
    q4 = len([r for r in robots if r["p"][0] > w // 2 and r["p"][1] < h // 2])

    return q1 * q2 * q3 * q4


def part2(robots):
    w = 101
    h = 103

    for i in range(1, 10001):
        robots = [add_vel(r, w, h) for r in robots]

        map = []
        for y in range(h):
            map.append([" "] * w)

        for r in robots:
            map[r["p"][1]][r["p"][0]] = "#"

        robots_per_line = [0] * h
        for r in robots:
            robots_per_line[r["p"][1]] += 1

        if any([robot_count >= 20 for robot_count in robots_per_line]):
            print(f"\n\n======={i}=======")
            print("\n".join(["".join(l) for l in map]))
            input()


def main():
    robots = read_input()

    ans1 = part1(robots)
    print(f"{ans1=}")

    ans2 = part2(robots)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
