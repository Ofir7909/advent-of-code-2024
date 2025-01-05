from collections import defaultdict, deque
from functools import wraps
import math


def read_input(input=None):
    if not input:
        with open("day21/input.txt", "r") as f:
            input = f.read()
    input = [l.strip() for l in input.strip().split("\n")]
    return input


def find_index_in_matrix(val, matrix):
    for y, line in enumerate(matrix):
        if val in line:
            return (line.index(val), y)
    return -1


numeric_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["", "0", "A"],
]
numeric_keypad_locations = {
    char: find_index_in_matrix(char, numeric_keypad) for char in "0123456789A"
}

directional_keypad = [
    ["", "^", "A"],
    ["<", "v", ">"],
]
directional_keypad_locations = {
    char: find_index_in_matrix(char, directional_keypad) for char in "<^>vA"
}

char_to_dir_map = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}


def BFS(graph, root):
    queue = deque([root])
    seen = {root}
    dist = defaultdict(lambda: math.inf)
    prev = defaultdict(lambda: None)

    dist[root] = 0

    while len(queue) > 0:
        v = queue.popleft()
        for u, move in graph[v]:
            if u not in seen:
                seen.add(u)
                dist[u] = dist[v] + 1
                prev[u] = (v, move)
                queue.append(u)

    return dist, prev


def part1(input):
    graph = {}
    for robot1 in "^>v<A":
        for robot2 in "^>v<A":
            for robot3 in "0123456789A":
                possible_moves = []
                # Pressing a dir
                for move in "^>v<":
                    try:
                        dir = char_to_dir_map[move]
                        r1_pos = directional_keypad_locations[robot1]
                        r1_newpos = (r1_pos[0] + dir[0], r1_pos[1] + dir[1])
                        if r1_newpos[0] < 0 or r1_newpos[1] < 0:
                            raise IndexError
                        new_r1 = directional_keypad[r1_newpos[1]][r1_newpos[0]]
                        if new_r1 == "":
                            continue
                        possible_moves.append(((new_r1, robot2, robot3), move))
                    except IndexError:
                        continue

                # Pressing A
                if robot1 in "^>v<":
                    try:
                        dir = char_to_dir_map[robot1]
                        r2_pos = directional_keypad_locations[robot2]
                        r2_newpos = (r2_pos[0] + dir[0], r2_pos[1] + dir[1])
                        if r2_newpos[0] < 0 or r2_newpos[1] < 0:
                            raise IndexError
                        new_r2 = directional_keypad[r2_newpos[1]][r2_newpos[0]]
                        if new_r2 != "":
                            possible_moves.append(((robot1, new_r2, robot3), "A"))
                    except IndexError:
                        pass
                else:
                    # Robot 1 pressing A
                    if robot2 in "^>v<":
                        try:
                            dir = char_to_dir_map[robot2]
                            r3_pos = numeric_keypad_locations[robot3]
                            r3_newpos = (r3_pos[0] + dir[0], r3_pos[1] + dir[1])
                            if r3_newpos[0] < 0 or r3_newpos[1] < 0:
                                raise IndexError
                            new_r3 = numeric_keypad[r3_newpos[1]][r3_newpos[0]]
                            if new_r3 != "":
                                possible_moves.append(((robot1, robot2, new_r3), "A"))
                        except IndexError:
                            pass

                graph[(robot1, robot2, robot3)] = possible_moves

    total_complexity = 0
    for code in input:
        presses_count = 0
        prev_char = "A"
        for char in code:
            dist, _ = BFS(graph, ("A", "A", prev_char))
            presses_count += dist[("A", "A", char)] + 1
            prev_char = char

        total_complexity += int(code[:-1]) * presses_count
    return total_complexity


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def calc_presses(index, from_key, to_key, numerical_index=25):
    if index == numerical_index:
        pos_start = numeric_keypad_locations[from_key]
        pos_end = numeric_keypad_locations[to_key]
    else:
        pos_start = directional_keypad_locations[from_key]
        pos_end = directional_keypad_locations[to_key]

    key_h = ">" if pos_start[0] < pos_end[0] else "<"
    key_v = "^" if pos_start[1] > pos_end[1] else "v"
    d_h = abs(pos_end[0] - pos_start[0])
    d_v = abs(pos_end[1] - pos_start[1])

    if index == 0:
        return d_h + d_v + 1

    if d_h == 0 and d_v == 0:
        return 1

    if d_h == 0:
        return (
            calc_presses(index - 1, "A", key_v)
            + (d_v - 1)
            + calc_presses(index - 1, key_v, "A")
        )

    if d_v == 0:
        return (
            calc_presses(index - 1, "A", key_h)
            + (d_h - 1)
            + calc_presses(index - 1, key_h, "A")
        )

    h_to_v = (
        calc_presses(index - 1, "A", key_h)
        + (d_h - 1)
        + calc_presses(index - 1, key_h, key_v)
        + (d_v - 1)
        + calc_presses(index - 1, key_v, "A")
    )
    v_to_h = (
        calc_presses(index - 1, "A", key_v)
        + (d_v - 1)
        + calc_presses(index - 1, key_v, key_h)
        + (d_h - 1)
        + calc_presses(index - 1, key_h, "A")
    )

    if (
        index == numerical_index
        and (pos_start[1] == 3 or pos_end[1] == 3)
        and (pos_start[0] == 0 or pos_end[0] == 0)
    ):
        if pos_start[0] < pos_end[0]:
            return h_to_v
        else:
            return v_to_h

    if (
        index != numerical_index
        and (pos_start[1] == 0 or pos_end[1] == 0)
        and (pos_start[0] == 0 or pos_end[0] == 0)
    ):
        if pos_start[0] < pos_end[0]:
            return h_to_v
        else:
            return v_to_h

    return min(h_to_v, v_to_h)


def part2(input):
    total_complexity = 0
    for code in input:
        presses_count = 0
        prev_char = "A"
        for char in code:
            presses_count += calc_presses(25, prev_char, char, 25)
            prev_char = char

        total_complexity += int(code[:-1]) * presses_count
    return total_complexity


def main():
    test_input = """
029A
980A
179A
456A
379A
""".strip()

    # input = read_input(test_input)
    input = read_input()

    ans1 = part1(input)
    print(f"{ans1=}")

    ans2 = part2(input)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
