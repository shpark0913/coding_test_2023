N = int(input())

coins = [500, 100, 50, 10]

count = 0

for i in range(4):
    Q = N // coins[i]
    R = N % coins[i]
    count += Q
    N = R

print(count)