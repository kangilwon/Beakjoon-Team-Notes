def solution(data):
    answer=[]
    deagi=[]
    print(data)
    

    
    for i in range(len(data)):

        for _ in range(data[i][2]):
            deagi.append(data[i][0])

        
    print(deagi)
    # print(len(data))
    # for i in range(n):
    #     num=data[i][2]
    #     if num
    #     deagi.append()
    # print(deagi)


    return answer

print(solution([[1, 0, 5],[2, 2, 2],[3, 3, 1],[4, 4, 1],[5, 10, 2]]))