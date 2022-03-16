def solution(arr):
    arr.sort()
    arr.reverse()
    print(arr)
    l=[]
    s=[]

    answer=0

    cnt=len(arr)%3
    print(cnt)
    if cnt !=0:
        for i in range(cnt):
            arr.pop()
        

    for i in range(1,len(arr)):
        if arr[i-1] == arr[i]:
            if arr[i] not in l:
                l.append(arr[i])
    for i in range(1,len(arr)):                
        if arr[i-1] != arr[i]:
            if arr[i] not in l:
                s.append(arr[i])

    # if len(s)==0:
    #     if len(l)%2!=0:
    #         l.pop()
    #         # for i in range(len(l))
    #         s.append(1)


    
    answer=sum(l)+len(s)

    print(l,s)
    return answer

print(solution([1,1,2,2,3,3,4,4,5,5,6,6]))