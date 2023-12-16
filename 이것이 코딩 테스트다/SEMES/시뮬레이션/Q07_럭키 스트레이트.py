N = input()

L, R = N[:len(N)//2], N[len(N)//2:]

L_sum, R_sum = 0, 0

for l in L:
    L_sum += int(l)

for r in R:
    R_sum += int(r)

if L_sum == R_sum:
    print("LUCKY")
else:
    print("READY")