def solution(scoville, K):
    answer = []
    scoville.sort()
    x=scoville.pop(0)
    while True:
        scoville.sort()
        if x >= K:
            answer.append(x)
            x=scoville.pop(0)
        else:
            a=min(x,scoville[0])
            b=max(x,scoville[0])
            x=a+(b*2)
            scoville.pop(0)
        if len(scoville)==0:
            break
        print(answer,x)
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))