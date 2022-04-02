def solution(dist):
    result= max(dist)
    answer = []
    sub=[]
    for _ in range(len(result)-1,-1,-1):
        a=result.index(max(result))
        sub.append(a)
        result[a]=-1
    
    answer.append(sub[::-1])
    answer.append(sub)
    answer.sort()
    return answer

print(solution([[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]))