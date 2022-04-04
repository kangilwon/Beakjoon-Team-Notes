def solution(priorities, location):
    answer = 0
    idx = [i for i in range(len(priorities))]
    val = priorities.copy()

    while True:
        if val[answer] < max(val[answer+1:]):
            idx.append(idx.pop(answer))
            val.append(val.pop(answer))
        else:
            answer += 1

        if val == sorted(val, reverse=True):
            break

    return idx.index(location)+1


print(solution([2, 1, 3, 2], 2))
