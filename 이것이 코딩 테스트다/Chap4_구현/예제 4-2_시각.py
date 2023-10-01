# N = int(input())

# h, m, s = 0, 0, 0
# ans = 0

# while (h != N or m != 59 or s != 59):
#     s += 1
#     if s == 60:
#         m += 1
#         s = 0
#     if m == 60:
#         h += 1
#         m = 0
#     if "3" in str(h) or "3" in str(m) or "3" in str(s):
#         ans += 1

# print(ans)

############################################################

h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 3이 포함되어 있다면 카운트 증가
            if "3" in str(i) + str(j) + str(k):
                count += 1

print(count)