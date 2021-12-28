def solution(truck, w):
    answer = [0 for i in range(len(w))]
    for i in range(len(w)):
        for j in range(len(truck)):
            if w[i]<=truck[j]:
                answer[i]=j+1
                truck[j]-=w[i]
                break
    for i in range(len(answer)):
        if answer[i]<0:
            answer[i]=-1
    return answer

truck=[2,7,4,9]
w=[7,6,8]
print(solution(truck,w))