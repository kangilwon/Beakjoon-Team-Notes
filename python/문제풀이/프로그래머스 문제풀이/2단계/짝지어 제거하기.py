def solution(s):
    answer = []
    cnt = 0
    for i in s:
        if len(answer) == 0:
            answer.append(i)
        elif answer[-1] == i:
            answer.pop()
        else:
            answer.append(i)
    if len(answer)==0:
        return 1
    else:
        return 0


print(solution('cdcd'))
