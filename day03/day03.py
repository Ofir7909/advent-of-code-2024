import re

def read_input():
    with open("day03/input.txt", "r") as f:
        s = [l.strip() for l in f.readlines()]
    return s

def extract_instructions(input):
    pattern = re.compile(r"(?P<mul>mul)\((?P<a>\d{1,3}),(?P<b>\d{1,3})\)|(?P<dont>don't\(\))|(?P<do>do\(\))")

    instructions = []
    for line in input:
        matches = [m.groupdict() for m in pattern.finditer(line)]
        for m in matches:
            if m['do'] != None:
                instructions.append(('do',))
            if m['dont'] != None:
                instructions.append(('dont',))
            if m['mul'] != None:
                instructions.append(('mul', int(m['a']), int(m['b'])))
        #instructions += [(int(m['a']), int(m['b'])) for m in matches]

    return instructions

def calculate_mul_sum(instructions):
    enabled = True
    sum = 0
    for ins in instructions:
        if enabled and ins[0] == "mul":
            sum += ins[1] * ins[2]
        elif ins[0] == "do":
            enabled = True
        elif ins[0] == "dont":
            enabled = False
    return sum
    #return sum(i[0] * i[1] for i in instructions)



if __name__ == "__main__":
    input = read_input()
    instructions = extract_instructions(input)
    print(instructions)
    print(f"{calculate_mul_sum(instructions)}")
