
def solution(b):

    temp=[]
    for i in range(1,b):
        temp.append(((i**2)+(b**2))**0.5)

    for i in temp:
        if i == int(i):
            answer=i
            break
        else:
            answer=-1

    return answer
    

b=12
print(solution(b))