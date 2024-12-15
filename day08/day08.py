import string
import itertools

def read_input():
    with open("day08/input.txt", "r") as f:
        input = [list(l.strip()) for l in f.readlines()]
    return input


def part1(input):
    n = len(input)
    m = len(input[0])
    antinodes = set()

    for chr in (string.ascii_letters + string.digits):

        nodes = set()
        for x in range(n):
            for y in range(m):
                if input[x][y] == chr:
                    nodes.add((x,y))
    
        
        for a,b in itertools.product(nodes, nodes):
            if a[0] <= b[0] and a[1] <= b[1]:
                continue
            
            diff = (b[0] - a[0], b[1] - a[1])

            point = (b[0] + diff[0], b[1] + diff[1])
            if point[0] in range(n) and point[1] in range(m):
                antinodes.add(point)
            point = (a[0] - diff[0], a[1] - diff[1])
            if point[0] in range(n) and point[1] in range(m):
                antinodes.add(point)
    return len(antinodes)




def part2(input):
    n = len(input)
    m = len(input[0])
    antinodes = set()

    for chr in (string.ascii_letters + string.digits):

        nodes = set()
        for x in range(n):
            for y in range(m):
                if input[x][y] == chr:
                    nodes.add((x,y))
    
        
        for a,b in itertools.product(nodes, nodes):
            if a[0] <= b[0] and a[1] <= b[1]:
                continue

            antinodes.add(a)
            antinodes.add(b)
            
            diff = (b[0] - a[0], b[1] - a[1])

            point = b
            while True:
                point = (point[0] + diff[0], point[1] + diff[1])
                if point[0] in range(n) and point[1] in range(m):
                    antinodes.add(point)
                else: 
                    break
            
            point = a
            while True:
                point = (point[0] - diff[0], point[1] - diff[1])
                if point[0] in range(n) and point[1] in range(m):
                    antinodes.add(point)
                else: 
                    break
    return len(antinodes)


def main():
    input = read_input()

#     input = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............""".split("\n")
#     input = [list(l) for l in input]

    ans1 = part1(input)
    print(f"{ans1=}")

    ans2 = part2(input)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
