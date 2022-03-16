
def solution(products,purchased):
    x=[]
    o=[]

    for i in purchased:
        for j in products:
            if i in j:
                q=list(j.split())

            
        x.append(q)
    print(x)
    for i in range(len(x)):
        for j in range(1,len(x[i])):
            print(x[i][j])
            if x[i][j] not in o:
                o.append(x[i][j])

    answer=''
    return answer

print(solution(["sofa red long", "blanket blue long", "towel red", "mattress long", "curtain blue long cheap"],	["towel", "mattress", "curtain"]))