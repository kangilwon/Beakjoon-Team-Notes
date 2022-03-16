def solution(money, costs):
    answer = []
    start=[]
    k=[]
    costs.reverse()

    n = money  # 현재금액
    count = 0

    array = [500, 100, 50, 10, 5, 1]  # 화폐단위 큰 단위부터
    array.reverse()
    for i in range(len(array)):
        c=costs[i]*array[i]
        start.append(c)
    array.reverse()

    for j in range(len(start)):
        k.append(start.index(min(start)))
        start[k[j]]=99999

    for i in k:
       
        count = n//array[i]*costs[i]  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기

        n %= array[i]
        answer.append(count)

    return sum(answer)

print(solution(4578, [1, 4, 99, 35, 50, 1000]))