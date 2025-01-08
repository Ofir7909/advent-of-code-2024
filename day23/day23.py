from collections import defaultdict


def read_input(input=None):
    if not input:
        with open("day23/input.txt", "r") as f:
            input = f.read().strip()
    pairs = [tuple(l.strip().split("-")) for l in input.split("\n")]
    return pairs


def part1(pairs):
    computers = set(c for p in pairs for c in p)

    triples_with_t = set()

    for p in pairs:
        if p[0][0] != "t" and p[1][0] != "t":
            continue
        for c in computers:
            if ((p[0], c) in pairs or (c, p[0]) in pairs) and (
                (p[1], c) in pairs or (c, p[1]) in pairs
            ):
                triple = tuple(sorted([*p, c]))
                triples_with_t.add(triple)

    return len(triples_with_t)


def bron_kerbosch(R, P, X, graph):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bron_kerbosch(
            R.union({v}), P.intersection(graph[v]), X.intersection(graph[v]), graph
        )
        X.add(v)


def part2(pairs):
    graph = defaultdict(lambda: [])
    for p in pairs:
        graph[p[0]].append(p[1])
        graph[p[1]].append(p[0])

    all_cliques = list(bron_kerbosch(set(), set(graph.keys()), set(), graph))
    max_clique_size = max(len(c) for c in all_cliques)

    max_clique: set
    for c in all_cliques:
        if max_clique_size == len(c):
            max_clique = c
            break

    return ",".join(sorted(max_clique))


def main():
    test_input = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
""".strip()

    # pairs = read_input(test_input)
    pairs = read_input()

    ans1 = part1(pairs)
    print(f"{ans1=}")

    ans2 = part2(pairs)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
