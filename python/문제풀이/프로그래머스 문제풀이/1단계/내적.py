def solution(a, b):
    for i in range(len(a)):
        a[i]*=b[i]
    return sum(a)

print(solution([-1,0,1]	, [1,0,-1]))