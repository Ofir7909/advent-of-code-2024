def read_input():
    with open("day04/input.txt", "r") as f:
        input = [l.strip() for l in f.readlines()]
    return input


def part1(word, matrix):
    count = 0
    n = len(matrix)
    m = len(matrix[0])

    def safe_matrix(y,x):
        if y < 0 or x < 0 or y >= n or x >= m:
            return ""
        return matrix[y][x]

    for y in range(n):
        for x in range(m):
            if matrix[y][x] != word[0]:
                continue

            flags = 0b11111111
            for i, c in enumerate(word[1:], 1):
                if safe_matrix(y, x+i) != c:
                        flags &= ~(1 << 0)
                if safe_matrix(y+i,x+i) != c:
                        flags &= ~(1 << 1)
                if safe_matrix(y+i,x) != c:
                        flags &= ~(1 << 2)
                if safe_matrix(y+i,x-i) != c:
                        flags &= ~(1 << 3)
                if safe_matrix(y,x-i) != c:
                        flags &= ~(1 << 4)
                if safe_matrix(y-i,x-i) != c:
                        flags &= ~(1 << 5)
                if safe_matrix(y-i,x) != c:
                        flags &= ~(1 << 6)
                if safe_matrix(y-i,x+i) != c:
                        flags &= ~(1 << 7)
            count += flags.bit_count()
    return count

def part2(matrix):
    count = 0
    n = len(matrix)
    m = len(matrix[0])

    def safe_matrix(y,x):
        if y < 0 or x < 0 or y >= n or x >= m:
            return ""
        return matrix[y][x]

    for y in range(n)[1:-1]:
        for x in range(m)[1:-1]:
            if matrix[y][x] != 'A':
                continue

            if safe_matrix(y-1, x-1) == safe_matrix(y+1, x-1) == "M" and safe_matrix(y-1, x+1) == safe_matrix(y+1, x+1) == "S":
                count += 1
            elif safe_matrix(y-1, x-1) == safe_matrix(y+1, x-1) == "S" and safe_matrix(y-1, x+1) == safe_matrix(y+1, x+1) == "M":
                count += 1
            elif safe_matrix(y-1, x-1) == safe_matrix(y-1, x+1) == "M" and safe_matrix(y+1, x-1) == safe_matrix(y+1, x+1) == "S":
                count += 1
            elif safe_matrix(y-1, x-1) == safe_matrix(y-1, x+1) == "S" and safe_matrix(y+1, x-1) == safe_matrix(y+1, x+1) == "M":
                count += 1
    return count
            


if __name__ == "__main__":
    input = read_input()

    ans1 = part1("XMAS", input)
    print(f"{ans1=}")

    ans2 = part2(input)
    print(f"{ans2=}")
