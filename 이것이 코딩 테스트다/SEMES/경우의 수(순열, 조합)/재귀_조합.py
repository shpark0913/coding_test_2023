def combination(arr, n):
    answer = []

    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        element = arr[i]
        for rest in combination(arr[i + 1:], n - 1):
            answer.append([element] + rest)
    
    return answer

ans = combination(["A", "A", "A", "B", "C"], 2)
print("ans", ans)
ans_tuple = [tuple(i) for i in ans]
ans_tuple = list(set(ans_tuple))
print("ans_tuple", ans_tuple)
ans_final = [list(i) for i in ans_tuple]
print("ans_final", ans_final)