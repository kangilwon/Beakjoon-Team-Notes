def solution(m, n, puddles):
    puddles=[[x,y] for [y,x] in puddles]
    home_route=[[0] * (m + 1) for i in range(n + 1)]
    home_route[1][1]=1
    for i in range(1, n + 1):
            for j in range(1, m + 1):
                print(home_route,i,j)
                if i == 1 and j == 1: continue 
                if [i,j] in puddles:home_route[i][j]=0
                else:home_route[i][j]=(home_route[i-1][j]+home_route[i][j-1])%1000000007

    
    return home_route[n][m]


print(solution(4, 3, []))
