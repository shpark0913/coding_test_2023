# s = input()
# i, j = s[0], int(s[1])

# move_types = ["A", "B", "C", "D", "E", "F", "G", "H"]
# dx = [2, 2, -2, -2, 1, -1, 1, -1]
# dy = [-1, 1, -1, 1, 2, 2, -2, -2]

# change_number = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# for k in range(len(change_number)):
#     if i == change_number[k]:
#         i = k

# count = 0

# for k in range(len(move_types)):
#     nx = i + dx[k]
#     ny = j + dy[k]
#     if nx < 1 or nx > 8 or ny < 1 or ny > 8:
#         continue
#     count += 1

# print(count)

##########################################################

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방ㅇ향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대해 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)