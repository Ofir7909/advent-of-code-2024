def read_input(input=None):
    if not input:
        with open("day17/input.txt", "r") as f:
            input = f.read().strip()
    reg_input = input.split("\n\n")[0]
    inst_input = input.split("\n\n")[1]

    registers = {
        line.split(":")[0].removeprefix("Register "): int(line.split(":")[1].strip())
        for line in reg_input.split("\n")
    }

    instructions = list(map(int, inst_input.removeprefix("Program: ").split(",")))
    return registers, instructions


def combo_operand(operand, registers):
    if 0 <= operand and operand <= 3:
        return operand
    if operand == 4:
        return registers["A"]
    if operand == 5:
        return registers["B"]
    if operand == 6:
        return registers["C"]
    if operand == 7:
        print("error combo operand 7 is invalid")


def part1(registers, instructions):
    pc = 0
    out = []
    while 0 <= pc < len(instructions):
        op_code = instructions[pc]
        operand = instructions[pc + 1]
        pc += 2
        match op_code:
            case 0:  # adv
                registers["A"] = registers["A"] // (
                    2 ** combo_operand(operand, registers)
                )
            case 1:  # bxl
                registers["B"] = registers["B"] ^ operand
            case 2:  # bst
                registers["B"] = combo_operand(operand, registers) % 8
            case 3:  # jnz
                if registers["A"] != 0:
                    pc = operand
            case 4:  # bxc
                registers["B"] = registers["B"] ^ registers["C"]
            case 5:  # out
                out.append(combo_operand(operand, registers) % 8)
            case 6:  # bdv
                registers["B"] = registers["A"] // (
                    2 ** combo_operand(operand, registers)
                )
            case 7:  # cdv
                registers["C"] = registers["A"] // (
                    2 ** combo_operand(operand, registers)
                )

    return ",".join(map(str, out))


def try_a_value_equivalent(val):
    A = val
    ans = ""
    while A != 0:
        B = A & 0b111
        C = A >> (B ^ 0b101)
        ans += str((B ^ C ^ 0b011) % 8)

        A = A >> 3
    return ans


def find_value_backtracking(instructions, values, i):
    if i < 0:
        return values
    for x in range(8):
        values[i] = x
        val = 0
        for v in values[::-1]:
            val = (val << 3) | v

        output = try_a_value_equivalent(val)
        print(output)
        if len(output) != len(instructions):
            continue
        if int(output[i]) == instructions[i]:
            ret_val = find_value_backtracking(instructions, values.copy(), i - 1)
            if ret_val:
                return ret_val
    return False


def part2(instructions):
    values = [0] * 16

    values = find_value_backtracking(instructions, values, 15)
    val = 0
    for v in values[::-1]:
        val = (val << 3) | v
    return val


def main():
    test_input = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
""".strip()

    # registers, instructions = read_input(test_input)
    registers, instructions = read_input()

    ans1 = part1(registers, instructions)
    print(f"{ans1=}")

    ans2 = part2(instructions)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
