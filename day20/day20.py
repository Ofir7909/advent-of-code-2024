from collections import defaultdict, deque
import itertools
import math
from re import A
from typing import Callable


def read_input(input=None):
    if not input:
        with open("day20/input.txt", "r") as f:
            input = f.read()
    maze = [list(l.strip()) for l in input.strip().split("\n")]
    return maze


def BFS(maze, root, adj: Callable):
    queue = deque([root])
    seen = {root}
    dist = defaultdict(lambda: math.inf)
    prev = defaultdict(lambda: None)

    dist[root] = 0

    while len(queue) > 0:
        v = queue.popleft()
        for u in adj(v):
            if u not in seen:
                seen.add(u)
                dist[u] = dist[v] + 1
                prev[u] = v
                queue.append(u)

    return dist, prev


def part1(maze):
    w, h = len(maze[0]), len(maze)
    start = tuple()
    end = tuple()

    for x, y in itertools.product(range(w), range(h)):
        if maze[y][x] == "S":
            start = (x, y)
        elif maze[y][x] == "E":
            end = (x, y)

    def adj(v):
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = v[0] + dir[0]
            ny = v[1] + dir[1]
            if maze[ny][nx] == "#":
                if v[2] == 0 and 1 <= nx < w - 1 and 1 <= ny < h - 1:
                    yield (nx, ny, 1)
            else:
                yield (nx, ny, v[2])

    dist1, prev1 = BFS(maze, (*start, 0), adj)
    dist2, prev2 = BFS(maze, (*end, 0), adj)

    original_shortest_dist = dist1[(*end, 0)]

    counter = 0
    for x, y in itertools.product(range(1, w - 1), range(1, h - 1)):
        if maze[y][x] == "#":
            d = dist1[(x, y, 1)] + dist2[(x, y, 1)]
            if not math.isinf(d) and original_shortest_dist - d >= 100:
                counter += 1
    return counter


def part2(maze):
    w, h = len(maze[0]), len(maze)
    start = tuple()
    end = tuple()

    for x, y in itertools.product(range(w), range(h)):
        if maze[y][x] == "S":
            maze[y][x] = "."
            start = (x, y)
        elif maze[y][x] == "E":
            end = (x, y)
            maze[y][x] = "."

    def adj(v):
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = v[0] + dir[0]
            ny = v[1] + dir[1]
            if maze[ny][nx] == "#":
                if v[2] == 0 and 1 <= nx < w - 1 and 1 <= ny < h - 1:
                    yield (nx, ny, 1)
            else:
                yield (nx, ny, v[2])

    dist1, prev1 = BFS(maze, (*start, 0), adj)
    dist2, prev2 = BFS(maze, (*end, 0), adj)

    original_shortest_dist = dist1[(*end, 0)]

    counter = 0
    for x1, y1 in itertools.product(range(1, w - 1), range(1, h - 1)):
        for x2, y2 in itertools.product(range(1, w - 1), range(1, h - 1)):
            cheat_seconds = abs(x2 - x1) + abs(y2 - y1)
            if 0 < cheat_seconds <= 20:
                if maze[y1][x1] == "." and maze[y2][x2] == ".":
                    d = dist1[(x1, y1, 0)] + dist2[(x2, y2, 0)] + cheat_seconds
                    if not math.isinf(d) and original_shortest_dist - d >= 100:
                        counter += 1

    return counter


def main():
    test_input = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
""".strip()

    # maze = read_input(test_input)
    maze = read_input()

    ans1 = part1(maze)
    print(f"{ans1=}")

    ans2 = part2(maze)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
