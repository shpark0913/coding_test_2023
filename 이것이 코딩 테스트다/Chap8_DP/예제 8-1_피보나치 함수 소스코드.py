# 피보나치 함수 재귀 함수로 구현
def fibo(x):
    if x in [1, 2]:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))