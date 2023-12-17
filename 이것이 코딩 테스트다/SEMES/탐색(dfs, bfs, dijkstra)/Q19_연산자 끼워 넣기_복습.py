from itertools import permutations

N = int(input())

max_value = - int(1e9)
min_value = int(1e9)

numbers = list(map(int, input().split()))

signs_number = list(map(int, input().split()))

signs = []

for i in range(4):
    if signs_number[i]:
        if i == 0:
            signs += ["+"] * signs_number[0]
        elif i == 1:
            signs += ["-"] * signs_number[1]
        elif i == 2:
            signs += ["*"] * signs_number[2]
        elif i == 3:
            signs += ["/"] * signs_number[3]

signs_permutations = list(set(permutations(signs)))

for permu in signs_permutations:
    value = numbers[0]
    for i in range(len(permu)):
        if permu[i] == "+":
            value += numbers[i + 1]
        elif permu[i] == "-":
            value -= numbers[i + 1]
        elif permu[i] == "*":
            value *= numbers[i + 1]
        elif permu[i] == "/":
            value = int(value / numbers[i + 1])
    if value < min_value:
        min_value = value
    if value > max_value:
        max_value = value

print(max_value)
print(min_value)

# 2
# 5 6
# 0 0 1 0

# 3
# 3 4 5
# 1 0 1 0

# 6
# 1 2 3 4 5 6
# 2 1 1 1