from collections import deque
import itertools
import math
import sys


def read_input(input=None):
    if not input:
        with open("day18/input.txt", "r") as f:
            input = f.read().strip()

    coords = [tuple(map(int, l.strip().split(","))) for l in input.split("\n")]
    return coords


def BFS(world, root):
    queue = deque([root])
    seen = {root}
    dist = {
        (x, y): sys.maxsize
        for x, y in itertools.product(range(71), range(71))
        if world[y][x] == 0
    }
    prev = {
        (x, y): None
        for x, y in itertools.product(range(71), range(71))
        if world[y][x] == 0
    }

    dist[root] = 0

    while len(queue) > 0:
        v = queue.popleft()
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = v[0] + dir[0]
            ny = v[1] + dir[1]
            if 0 <= nx <= 70 and 0 <= ny <= 70 and world[ny][nx] != 1:
                node = (nx, ny)
                if node not in seen:
                    seen.add(node)
                    dist[node] = dist[v] + 1
                    prev[node] = v
                    queue.append(node)

    return dist, prev


def part1(coords):
    world = [[0 for _ in range(71)] for _ in range(71)]
    for i in range(1024):
        x, y = coords[i]
        world[y][x] = 1

    dist, prev = BFS(world, (0, 0))
    return dist[(70, 70)]


def part2(coords):
    l = 1024
    r = len(coords)

    while l < r:
        m = math.ceil((l + r) / 2)
        world = [[0 for _ in range(71)] for _ in range(71)]
        for i in range(m):
            x, y = coords[i]
            world[y][x] = 1

        dist, prev = BFS(world, (0, 0))
        if dist[(70, 70)] > 100_000:  # no_path
            r = m - 1
        else:
            l = m

    return coords[l]


def main():
    test_input = """
""".strip()

    # input = read_input(test_input)
    coords = read_input()

    ans1 = part1(coords)
    print(f"{ans1=}")

    ans2 = part2(coords)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
