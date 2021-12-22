def solution(n):
    answer = str(n)
    answer=list(map(int,answer))
    answer.sort(reverse=True)
    answer=''.join(map(str,answer))
    answer=int(answer)
    return answer

def solution(numbers):
    num=[0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        if i in num:
            num.remove(i)

    answer = sum(num)

    return answer

a=[5,8,4,0,6,7,9]
print(solution(a))