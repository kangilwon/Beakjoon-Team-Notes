def solution(progresses, speeds):
    answer = []
    day=0
    cnt=0
    while len(progresses)>0:
        if progresses[0] + day*speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt+=1  
        else:
            day+=1
            if cnt > 0:
                answer.append(cnt)
                cnt=0
    answer.append(cnt)
    
    
    return answer

print(solution([93, 30, 55,98,3,99], [1, 30, 5, 1,1,1]))