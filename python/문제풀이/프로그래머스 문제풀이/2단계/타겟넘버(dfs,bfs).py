count = 0

def dfs(idx,result,numbers,target):
    global count
    n=len(numbers)  
    if n==idx:
        if result == target:
            count+=1
        return  

    dfs(idx+1,result+numbers[idx],numbers,target)
    dfs(idx+1,result-numbers[idx],numbers,target)
    
def solution(numbers, target):
    global count
    dfs(0,0,numbers,target)
    return count

print(solution([4,1,2,1],4))