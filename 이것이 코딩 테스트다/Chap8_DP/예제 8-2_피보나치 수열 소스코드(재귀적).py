# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현 (탑다운)
def fibo(x):
    # 종료 조건 : 1 혹은 2일 때 1을 반환
    if x in [1, 2]:
        return 1
    if d[x]:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))