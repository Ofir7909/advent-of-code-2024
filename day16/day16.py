from math import fabs
import sys


def read_input(input=None):
    if not input:
        with open("day16/input.txt", "r") as f:
            input = f.read().strip()
    maze = [list(l) for l in input.split("\n")]
    return maze


def dijkstra(graph: dict, start) -> int:
    dist = {v: sys.maxsize for v in graph.keys()}
    prev = {v: None for v in graph.keys()}
    queue = [v for v in graph.keys()]

    dist[start] = 0

    while len(queue) > 0:
        u = min([(u, dist[u]) for u in queue], key=lambda tup: tup[1])[0]
        queue.remove(u)

        for v, cost in graph[u]:
            if v not in queue:
                continue
            alt = dist[u] + cost
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist, prev


def gen_graph(maze, reverse=False):
    graph = {}
    start = ()
    end = ()
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "#":
                continue
            if cell == "E":
                end = (x, y)
            if cell == "S":
                start = (x, y)

            for rot in range(4):
                edges = []
                edges.append
                if not reverse:
                    if rot == 0 and maze[y][x + 1] != "#":
                        edges.append(((x + 1, y, rot), 1))
                    if rot == 1 and maze[y + 1][x] != "#":
                        edges.append(((x, y + 1, rot), 1))
                    if rot == 2 and maze[y][x - 1] != "#":
                        edges.append(((x - 1, y, rot), 1))
                    if rot == 3 and maze[y - 1][x] != "#":
                        edges.append(((x, y - 1, rot), 1))
                else:
                    if rot == 0 and maze[y][x - 1] != "#":
                        edges.append(((x - 1, y, rot), 1))
                    if rot == 1 and maze[y - 1][x] != "#":
                        edges.append(((x, y - 1, rot), 1))
                    if rot == 2 and maze[y][x + 1] != "#":
                        edges.append(((x + 1, y, rot), 1))
                    if rot == 3 and maze[y + 1][x] != "#":
                        edges.append(((x, y + 1, rot), 1))

                edges.append(((x, y, (rot + 1) % 4), 1000))
                edges.append(((x, y, (rot - 1) % 4), 1000))

                graph[(x, y, rot)] = edges

    graph[(start[0], start[1], 0)].append(("start", 0))
    graph["start"] = [((start[0], start[1], 0), 0)]

    graph["end"] = [((end[0], end[1], rot), 0) for rot in range(4)]
    for rot in range(4):
        graph[(end[0], end[1], rot)].append(("end", 0))

    return graph


def part1(maze):
    graph = gen_graph(maze)
    dist, prev = dijkstra(graph, "start")
    return dist["end"]


def floyd_warshall(graph: dict):
    verticies = list(graph.keys())
    n = len(verticies)
    dist = [[0x0FFFFFFF for j in range(n)] for i in range(n)]

    for v in verticies:
        for u, cost in graph[v]:
            i = verticies.index(v)
            j = verticies.index(u)
            dist[i][j] = cost

    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        print(k)
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def part2(maze):
    graph1 = gen_graph(maze)
    dist1, _ = dijkstra(graph1, "start")
    graph2 = gen_graph(maze, reverse=True)
    dist2, _ = dijkstra(graph2, "end")

    min_dist = dist1["end"]

    nodes = set()

    num_nodes_on_shortest_path = 0
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "#":
                continue
            for rot in range(4):
                u = (x, y, rot)
                if dist1[u] + dist2[u] == min_dist:
                    num_nodes_on_shortest_path += 1
                    nodes.add((x, y))
                    break

    for node in nodes:
        maze[node[1]][node[0]] = "O"
    print("\n".join(["".join(row) for row in maze]))
    return num_nodes_on_shortest_path


def main():
    test_input = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
    # maze = read_input(test_input.strip())
    maze = read_input()

    ans1 = part1(maze)
    print(f"{ans1=}")

    ans2 = part2(maze)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
