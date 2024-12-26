import copy
import numpy as np


def read_input():
    with open("day15/input.txt", "r") as f:
        input = f.read().split("\n\n")
    world_input = input[0]
    moves_input = input[1]

    world = [list(l) for l in world_input.split("\n")]
    moves = list(moves_input.replace("\n", ""))
    return world, moves


directions = {
    "^": np.array([0, -1]),
    ">": np.array([1, 0]),
    "v": np.array([0, 1]),
    "<": np.array([-1, 0]),
}


def try_move(world, pos: np.array, move) -> bool:
    dir = directions[move]
    next_pos = pos + dir
    if world[next_pos[1]][next_pos[0]] == "#":
        return False
    if world[next_pos[1]][next_pos[0]] == ".":
        world[next_pos[1]][next_pos[0]] = world[pos[1]][pos[0]]
        world[pos[1]][pos[0]] = "."
        return True
    if world[next_pos[1]][next_pos[0]] == "O":
        if not try_move(world, next_pos, move):
            return False
        world[next_pos[1]][next_pos[0]] = world[pos[1]][pos[0]]
        world[pos[1]][pos[0]] = "."
        return True


def part1(world, moves):
    robot_pos = np.array([0, 0])
    for y in range(len(world)):
        if "@" in world[y]:
            robot_pos = np.array([world[y].index("@"), y])

    for move in moves:
        moved = try_move(world, robot_pos, move)
        if moved:
            robot_pos += directions[move]

    gps_coords = [
        y * 100 + x
        for y, row in enumerate(world)
        for x, symbol in enumerate(row)
        if symbol == "O"
    ]
    return sum(gps_coords)


def can_move(world, pos: np.array, move) -> bool:
    dir = directions[move]
    next_pos = pos + dir
    if world[next_pos[1]][next_pos[0]] == "#":
        return False
    if world[next_pos[1]][next_pos[0]] == ".":
        return True
    if world[next_pos[1]][next_pos[0]] in ["[", "]"]:
        if move in ["<", ">"]:
            return can_move(world, next_pos, move)
        elif world[next_pos[1]][next_pos[0]] == "[":
            return can_move(world, next_pos, move) and can_move(
                world, next_pos + np.array([1, 0]), move
            )
        else:
            return can_move(world, next_pos + np.array([-1, 0]), move) and can_move(
                world, next_pos, move
            )
    print("error")


def do_move(world, pos: np.array, move):
    dir = directions[move]
    next_pos = pos + dir
    if world[next_pos[1]][next_pos[0]] == ".":
        pass
    elif world[next_pos[1]][next_pos[0]] in ["[", "]"]:
        if move in ["<", ">"]:
            do_move(world, next_pos, move)
        elif world[next_pos[1]][next_pos[0]] == "[":
            do_move(world, next_pos, move)
            do_move(world, next_pos + np.array([1, 0]), move)

        else:
            do_move(world, next_pos + np.array([-1, 0]), move)
            do_move(world, next_pos, move)
    else:
        print("error")
    world[next_pos[1]][next_pos[0]] = world[pos[1]][pos[0]]
    world[pos[1]][pos[0]] = "."
    return


def part2(world, moves):
    world_str = "\n".join(["".join(row) for row in world])
    world_str = (
        world_str.replace("#", "##")
        .replace("O", "[]")
        .replace(".", "..")
        .replace("@", "@.")
    )
    world = [list(l) for l in world_str.split("\n")]

    robot_pos = np.array([0, 0])
    for y in range(len(world)):
        if "@" in world[y]:
            robot_pos = np.array([world[y].index("@"), y])

    for move in moves:
        if can_move(world, robot_pos, move):
            do_move(world, robot_pos, move)
            robot_pos += directions[move]

    gps_coords = [
        y * 100 + x
        for y, row in enumerate(world)
        for x, symbol in enumerate(row)
        if symbol == "["
    ]
    return sum(gps_coords)


def main():
    world, moves = read_input()

    ans1 = part1(copy.deepcopy(world), moves)
    print(f"{ans1=}")

    ans2 = part2(copy.deepcopy(world), moves)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
