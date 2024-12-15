import copy

def read_input():
    with open("day06/input.txt", "r") as f:
        input = [list(l.strip()) for l in f.readlines()]
    return input


def part1(map_matrix):
    n = len(map_matrix)
    m = len(map_matrix[0])

    # find guard
    for y,line in enumerate(map_matrix):
        if "^" in line:
            guard_x = line.index("^")
            guard_y = y
    
    while 0 <= guard_x and guard_x < m and 0 <= guard_y and guard_y < n:
        guard_symbol = map_matrix[guard_y][guard_x]
        if guard_symbol == "^":
            new_x, new_y = guard_x, guard_y-1 
        elif guard_symbol == ">":
            new_x, new_y = guard_x+1, guard_y
        elif guard_symbol == "v":
            new_x, new_y = guard_x, guard_y+1
        elif guard_symbol == "<":
            new_x, new_y = guard_x-1, guard_y
        else:
            print("error, unknown character: ", guard_symbol)

        map_matrix[guard_y][guard_x] = "X"
        
        if not (0 <= new_x and new_x < m and 0 <= new_y and new_y < n):
            break
            
        
        
        if map_matrix[new_y][new_x] == "#":
            guard_symbol = "^>v<"[("^>v<".index(guard_symbol) + 1) % 4]
        else:
            guard_x, guard_y = new_x, new_y

        map_matrix[guard_y][guard_x] = guard_symbol
    
    return sum([l.count("X") for l in map_matrix])
        

    
    
        

def part2(original_map_matrix, solved_map):
    n = len(original_map_matrix)
    m = len(original_map_matrix[0])

    counter = 0
    for i in range(n):
        for j in range(m):
            if i==85 and j==61:
                continue
            
            if solved_map[i][j] != "X":
                continue
            map_matrix = copy.deepcopy(original_map_matrix)
            map_matrix[i][j] = "#"

            # find guard
            for y,line in enumerate(map_matrix):
                if "^" in line:
                    guard_x = line.index("^")
                    guard_y = y
            
            loop_count = 0
            while 0 <= guard_x and guard_x < m and 0 <= guard_y and guard_y < n:
                loop_count += 1
                if loop_count >= n*m:
                    counter += 1
                    break
                guard_symbol = map_matrix[guard_y][guard_x]
                if guard_symbol == "^":
                    new_x, new_y = guard_x, guard_y-1 
                elif guard_symbol == ">":
                    new_x, new_y = guard_x+1, guard_y
                elif guard_symbol == "v":
                    new_x, new_y = guard_x, guard_y+1
                elif guard_symbol == "<":
                    new_x, new_y = guard_x-1, guard_y
                else:
                    print("error, unknown character: ", guard_symbol)

                map_matrix[guard_y][guard_x] = "X"
                
                if not (0 <= new_x and new_x < m and 0 <= new_y and new_y < n):
                    break
                
                if map_matrix[new_y][new_x] == "#":
                    guard_symbol = "^>v<"[("^>v<".index(guard_symbol) + 1) % 4]
                else:
                    guard_x, guard_y = new_x, new_y

                map_matrix[guard_y][guard_x] = guard_symbol

            print(i, j, sum([l.count("X") for l in map_matrix]))
    
    return counter

def main():
    map_matrix = read_input()

    solved_map = copy.deepcopy(map_matrix)
    ans1 = part1(solved_map)
    print(f"{ans1=}")

    ans2 = part2(copy.deepcopy(map_matrix), solved_map)
    print(f"{ans2=}")

if __name__ == "__main__":
    main()
