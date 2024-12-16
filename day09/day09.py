import enum
import itertools


def read_input():
    with open("day09/input.txt", "r") as f:
        input = [int(n) for n in f.read().strip()]
    return input


def part1(input):
    if len(input) % 2 == 1:
        input.append(0)

    new_disk = []
    i = 0
    for block_size, free_size in itertools.batched(input, 2):
        new_disk += [i] * block_size + [-1] * free_size
        i += 1

    i = 0
    j = len(new_disk) - 1
    while i <= j:
        if new_disk[j] == -1:
            j -= 1
            continue
        if new_disk[i] != -1:
            i += 1
            continue

        new_disk[i], new_disk[j] = new_disk[j], new_disk[i]
        j -= 1
        i += 1

    return sum([k * v for k, v in enumerate(new_disk) if v != -1])


def part2(input):
    if len(input) % 2 == 1:
        input.append(0)

    new_disk = []
    i = 0
    for block_size, free_size in itertools.batched(input, 2):
        new_disk += [(i, block_size), (-1, free_size)]
        i += 1

    j = len(new_disk) - 1
    while 0 <= j:
        block = new_disk[j]
        if block[0] == -1:
            j -= 1
            continue

        i = 0
        while i < j:
            if new_disk[i][0] != -1 or block[1] > new_disk[i][1]:
                i += 1
                continue
            new_disk[i] = (-1, new_disk[i][1] - new_disk[j][1])
            new_disk[j] = (-1, block[1])
            new_disk.insert(i, block)
            break

        j -= 1

    new_disk = [[block] * count for block, count in new_disk]
    new_disk = [x for xl in new_disk for x in xl]
    return sum([k * v for k, v in enumerate(new_disk) if v != -1])


def main():
    input = read_input()
    # input = [int(c) for c in "2333133121414131402"]

    ans1 = part1(input)
    print(f"{ans1=}")

    ans2 = part2(input)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
