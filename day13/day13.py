import re
import itertools
from ortools.sat.python import cp_model


def read_input():
    with open("day13/input.txt", "r") as f:
        input = f.read().split("\n\n")

    machines = []
    for m in input:
        a = tuple(map(int, re.search(r"Button A: X\+(\d+), Y\+(\d+)", m).groups()))
        b = tuple(map(int, re.search(r"Button B: X\+(\d+), Y\+(\d+)", m).groups()))
        prize = tuple(map(int, re.search(r"Prize: X=(\d+), Y=(\d+)", m).groups()))
        machines.append({"a": a, "b": b, "prize": prize})

    return machines


def part1(machines):
    total_tokens = 0
    for m in machines:
        total_tokens += min(
            [
                3 * i + j
                for i, j in itertools.product(range(101), range(101))
                if i * m["a"][0] + j * m["b"][0] == m["prize"][0]
                and i * m["a"][1] + j * m["b"][1] == m["prize"][1]
            ],
            default=0,
        )
    return total_tokens


def part2(machines):
    total_tokens = 0
    for m in machines:
        m["prize"] = (m["prize"][0] + 10000000000000, m["prize"][1] + 10000000000000)

        model = cp_model.CpModel()

        i = model.NewIntVar(0, 20000000000000, "i")
        j = model.NewIntVar(0, 20000000000000, "j")

        model.Add(i * m["a"][0] + j * m["b"][0] == m["prize"][0])
        model.Add(i * m["a"][1] + j * m["b"][1] == m["prize"][1])

        model.Minimize(3 * i + j)

        solver = cp_model.CpSolver()
        status = solver.Solve(model)

        if status == cp_model.INFEASIBLE:
            continue

        total_tokens += solver.ObjectiveValue()

    return total_tokens


def main():
    machines = read_input()

    ans1 = part1(machines)
    print(f"{ans1=}")

    ans2 = part2(machines)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
