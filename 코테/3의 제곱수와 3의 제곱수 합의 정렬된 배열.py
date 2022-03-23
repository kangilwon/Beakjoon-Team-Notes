

answer=[]
def solution(n):
    
    global answer
    power_3=[]
    for i in range(n):
        power_3.append(3**i)
    result=fibo(n,power_3)
    return result

def fibo(x,list):
    sumlist=[]
    k=0
    for i in range(len(list)):
        k=sum(list[:len(list)-i])
        sumlist.append(k)
    for i in list:
        for j in list:
            if i != j:
                if i+j not in sumlist:
                    sumlist.append(i+j)
    answer=list+sumlist
    answer.sort()
    print(answer)
    return answer[x-1]

print(solution(4))