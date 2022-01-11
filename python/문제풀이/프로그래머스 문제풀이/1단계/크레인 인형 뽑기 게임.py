
def solution(board, moves):
    point_list=[]
    answer = 0
    
    for i in moves:
        for j in board:
            x = i-1
            if j[x] == 0:
                continue
            else:
                point_list.append(j[x])
                j[x] = 0
                break

    if len(point_list)>1:
        same_list=[point_list[0]]
        for i in range(1,len(point_list)):
            if same_list==[]:
                    same_list.append(point_list[i])
                    continue
            else:
                if same_list[-1] != point_list[i]:
                    same_list.append(point_list[i])
        
                else:
                    same_list.pop()
                    answer+=2
    else:
        True
        

    return answer

print(solution([[0,0,0,0],[1,0,0,0],[1,0,0,0],[1,1,1,0]],[1,3,1,2,1,4]))