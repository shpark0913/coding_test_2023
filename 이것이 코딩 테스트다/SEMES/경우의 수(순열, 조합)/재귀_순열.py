def permutation(arr, n):
    answer = []

    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        element = arr[i]
        for rest in permutation(arr[:i] + arr[i + 1:], n - 1):
            answer.append([element] + rest)
    
    return answer

print(permutation([1, 2, 3, 4, 5], 2))
print(len(permutation([1, 2, 3, 4, 5], 2)))