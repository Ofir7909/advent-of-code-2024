from collections import defaultdict
from pprint import pprint


def read_input(input=None):
    if not input:
        with open("day24/input.txt", "r") as f:
            input = f.read().strip()
    i1, i2 = input.split("\n\n")

    wires = {line.split(":")[0]: int(line.split(":")[1]) for line in i1.split("\n")}
    gates = [line.split() for line in i2.split("\n")]
    for g in gates:
        g.pop(3)
    return wires, gates


def toposort(nodes, adjs):
    def DFS(v):
        seen.add(v)
        for u in adjs(v):
            if u not in seen:
                DFS(u)
        sorted_list.append(v)

    sorted_list = []
    seen = set()

    for v in nodes:
        if v not in seen:
            DFS(v)

    return list(reversed(sorted_list))


def part1(wires: dict, gates: list):
    def adjs(v):
        for g in gates:
            if v == g[0] or v == g[2]:
                yield g[3]

    def sim_gate(gate):
        if gate[1] == "OR":
            return int(wires[gate[0]] or wires[gate[2]])
        elif gate[1] == "AND":
            return int(wires[gate[0]] and wires[gate[2]])
        elif gate[1] == "XOR":
            return int(wires[gate[0]] != wires[gate[2]])
        print("error")

    nodes = [g[3] for g in gates]

    sorted_order = toposort(nodes, adjs)

    for wire in sorted_order:
        gate = next(g for g in gates if g[3] == wire)
        wires[wire] = sim_gate(gate)

    z_wires = reversed(sorted(filter(lambda w: w[0] == "z", wires)))
    bin_str = ""
    for w in z_wires:
        bin_str += str(wires[w])

    return int(bin_str, 2)


def wire_name(prefix: str, i):
    return prefix + str(i).zfill(2)


def part2(wires, gates):
    # dict: wire_name: (created_with_gate, times_used, used_in_gates)
    wires_used_freq = {}
    for g in gates:
        wires_used_freq[g[3]] = [g[1], 0, []]

    for g in gates:
        if g[0][0] not in "xy":
            wires_used_freq[g[0]][1] += 1
            wires_used_freq[g[0]][2].append(g[1])
            wires_used_freq[g[2]][1] += 1
            wires_used_freq[g[2]][2].append(g[1])

    wrong_wires = set(["qbw"])
    for wire, v in wires_used_freq.items():
        false_positives = ["z45", "sgv"]
        if wire in false_positives:
            continue
        gate, count, used_in = v
        # z gates created from XOR
        if wire[0] == "z" and gate != "XOR":
            wrong_wires.add(wire)

        # XOR_IN used twice (AND and XOR)
        if wire[0] != "z" and gate == "XOR":
            if count != 2 or "AND" not in used_in or "XOR" not in used_in:
                wrong_wires.add(wire)

        # AND gates used once (OR)
        if gate == "AND":
            if count != 1 or "OR" not in used_in:
                wrong_wires.add(wire)

        # OR gates used twice (AND and XOR) (carry)
        if gate == "OR":
            if count != 2 or "AND" not in used_in or "XOR" not in used_in:
                wrong_wires.add(wire)

    return ",".join(sorted(wrong_wires))


def main():
    wires, gates = read_input()

    ans1 = part1(wires, gates)
    print(f"{ans1=}")

    ans2 = part2(wires, gates)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
