list1 = []
list2 = []

with open("day01/input1.txt", "r") as f:
    for line in f:
        a,b = line.split()
        list1.append(int(a))
        list2.append(int(b))

appearances = {}
for n in list2:
    if n in appearances:
        appearances[n] += 1
    else:
        appearances[n] = 1

sum = 0
for n in list1:
    if n in appearances:
        sum += n * appearances[n]
print(sum)