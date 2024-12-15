left = []
right = []

with open("day01/input1.txt", "r") as f:
    for line in f:
        l,r = line.split()
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()

ans = sum(abs(l-r) for l,r in zip(left,right))
print(ans)