import re


def solution(answers):
    answer = [1,2,3]
    a=[1, 2, 3, 4, 5]; b=[2, 1, 2, 3, 2, 4, 2, 5]; c=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a_cnt=0; b_cnt=0; c_cnt=0
    for i in range(len(answers)):
        if answers[i] == a[i]:
            a_cnt+=1
        if answers[i] == b[i]:
            b_cnt+=1
        if answers[i] == c[i]:
            c_cnt+=1
    if a_cnt == b_cnt == c_cnt:
       return answer
    elif b_cnt<a_cnt>c_cnt:
        return list(answer[0])
    elif a_cnt<b_cnt>c_cnt:
        return answer[2]
    elif a_cnt<c_cnt>b_cnt:
        return answers[3]


print(solution([1,2,3,4,5]))