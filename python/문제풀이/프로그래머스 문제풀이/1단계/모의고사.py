def solution(answers):
    answer = []
    a=[1, 2, 3, 4, 5]; b=[2, 1, 2, 3, 2, 4, 2, 5]; c=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a_cnt=0; b_cnt=0; c_cnt=0
    for i in range(len(answers)):
        if answers[i] == a[i]:
            a_cnt+=1
        if answers[i] == b[i]:
            b_cnt+=1
        if answers[i] == c[i]:
            c_cnt+=1
    if a_cnt > b_cnt and a_cnt > c_cnt:
        answer.append(a_cnt)
    if b_cnt > a_cnt and b_cnt > c_cnt:
        answer.append(b_cnt)
    if c_cnt > b_cnt and c_cnt > a_cnt:
        answer.append(c_cnt)
    if a_cnt == b_cnt == c_cnt:
        answer.append(a_cnt)
    
    return answer
print(solution([1,2,3,4,5]))