def read_input():

    with open("day05/input.txt", "r") as f:
        input = [l.strip() for l in f.readlines()]
    i = input.index("")
    rules = [tuple(map(int, l.split("|"))) for l in input[:i]]
    printing_order = [list(map(int, l.split(","))) for l in input[i+1:]]
    return rules, printing_order


def is_valid_order(order, rules):
    for i, a in enumerate(order):
        for b in order[i+1:]:
            if (b,a) in rules:
                return False
    return True


def part1(rules, printing_order):
    return sum([o[len(o)//2] for o in filter(lambda o: is_valid_order(o, rules),printing_order)])


def topological_sort(verts: set, edges: set[tuple]):
    topo_order = []
    visited = set()
    
    def topo_dfs(verts,edges,node):
        visited.add(node)
        neighbors = [v for (u,v) in edges if u == node]
        for neighbor in neighbors:
            if neighbor not in visited:
                topo_dfs(verts,edges, neighbor)
        topo_order.append(node)
    
    for node in verts:
        if node not in visited:
            topo_dfs(verts, edges, node)
    return topo_order


def fix_order(order, rules):
    v = order
    e = list(filter(lambda r: r[0] in v and r[1] in v, rules))
    
    return topological_sort(v,e)


def part2(rules, printing_order):

    return sum([o[len(o)//2] for o in map(lambda o: fix_order(o, rules), filter(lambda o: not is_valid_order(o, rules),printing_order))])



def main():
    rules, printing_order = read_input()
    #print(rules)
    #print(printing_order)

    ans1 = part1(rules, printing_order)
    print(f"{ans1=}")

    ans2 = part2(rules, printing_order)
    print(f"{ans2=}")

if __name__ == "__main__":
    main()