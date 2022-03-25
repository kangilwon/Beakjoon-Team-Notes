def solution(triangle):
    answer = triangle[0][0]

    for i in range(1,len(triangle)):
        
        for j in range(len(triangle[i])): 
            if j==0:
                triangle[i][0]+=triangle[i-1][0]
            elif j==len(triangle[i])-1:
                triangle[i][len(triangle[i])-1]+=triangle[i-1][len(triangle[i-1])-1]
            else:
                if triangle[i-1][j-1]<triangle[i-1][j]:
                    answer=triangle[i-1][j]
                else:
                    answer=triangle[i-1][j-1]
                triangle[i][j]+=answer
      

    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
# 나폴리탄괴담