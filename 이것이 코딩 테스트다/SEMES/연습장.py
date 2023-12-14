# # def permutation(arr, n):
# #     answer = []

# #     if n == 0:
# #         return [[]]
    
# #     for i in range(len(arr)):
# #         element = arr[i]
# #         for rest in permutation(arr, n - 1):
# #         # for rest in permutation(arr[:i] + arr[i + 1:], n - 1):
# #             answer.append([element] + rest)
    
# #     return answer

# # print(permutation([1, 2, 3], 3))

# def combination(arr, n):
#     answer = []

#     if n == 0:
#         return [[]]
    
#     for i in range(len(arr)):
#         element = arr[i]
#         for rest in combination(arr[i:], n - 1):
#         # for rest in combination(arr[i + 1:], n - 1):
#             answer.append([element] + rest)
    
#     return answer

# print(combination([1, 2, 3, 4], 2))

import heapq

INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[] for _ in range(N + 1)]

distance = [[INF] ]