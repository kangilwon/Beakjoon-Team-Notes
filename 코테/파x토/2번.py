def solution(grade):
    answer = [0 for i in range(len(grade))]
    stu_max=max(grade)
    num=1
    cnt=0
    
    for j in range(stu_max):
        for i in range(len(grade)):
            if grade[i]==stu_max:
                answer[i]=num
                cnt+=1
        num+=cnt
        cnt=0
        stu_max-=1 

    return answer

grade=[2,2,1]
print(solution(grade))