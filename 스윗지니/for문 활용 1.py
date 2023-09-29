# 기존 내가 작성한 코드. if 문에서 11 안에 1이 1번 들어있다고 카운트하므로 잘못된 코드이다.
# def solution(i, j, k):
#     answer = 0
#     for num in range(i, j + 1):
#         if str(k) in str(num):
#             answer += 1
#     return answer

# def solution(i, j, k):
#     answer = 0
#     k = str(k)
#     for num in range(i, j + 1):
#         # count 잘 사용하기. 유용하다.
#         answer += str(num).count(k)
#     return answer

# i, j, k = map(int, input().split())

# print(solution(i, j, k))

###################################################################################################

def solution(num_list, num):
    answers = []
    for i in range(len(num_list)//num):
        answer = []
        for j in range(num):
            answer.append(num * i + j)
        answers.append(answer)
    return answers

print(solution(num_list, num))