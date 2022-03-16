def solution(width, height, diagonals):
    answer = 0
    for i in range(width):
        for j in range(height):
            print(i,',',j,' ', end=' ')
        print()
        print()

    return answer


print(solution(5,	5,	[[1,1],[2,2]]))