def solution(absolutes, signs):
    for i in range(len(signs)):
        absolutes[i] *= 1 if signs[i] == 'true' else -1
                
    return sum(absolutes)

print(solution([4,7,12],['true','false','true']))