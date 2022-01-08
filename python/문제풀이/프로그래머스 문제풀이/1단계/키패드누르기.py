def solution(numbers, hand):
    answer = ''
    r_now = '#'
    l_now = '*'

    r_return = [3, 6, 9]
    l_return = [1, 4, 7]
    r_or_l = [2, 5, 8, 0]

    for i in range(len(numbers)):
        if numbers[i] in r_return:
            answer += 'R'
            r_now = i
        elif numbers[i] in l_return:
            answer += 'L'
            l_now = i
        else:
            if numbers[i] == 2:  # 1,3,5,8,0
                if r_now == '#':
                    if numbers[l_now] in [1, 3, 5]:
                        answer += 'L'
                        l_now = i
                elif l_now == '*':
                    if numbers[r_now] in [1, 3, 5]:
                        answer += 'R'
                        r_now = i
                elif numbers[r_now] in [1, 3, 5] or numbers[l_now] in [1, 3, 5]:
                    if numbers[r_now] in [1, 3, 5] and numbers[l_now] in [1, 3, 5]:
                        if hand == 'right':
                            answer += 'R'
                            r_now = i
                        else:
                            answer += 'L'
                            l_now = i
                    elif numbers[r_now] in [1, 3, 5]:
                        answer += 'R'
                        r_now = i
                    elif numbers[l_now] in [1, 3, 5]:
                        answer += 'L'
                        l_now = i
                else:
                    if numbers[l_now]+2 == numbers[r_now]:
                        if hand == 'right':
                            answer += 'R'
                            r_now = i
                        else:
                            answer += 'L'
                            l_now = i
                    elif l_now < r_now:
                            answer += 'L'
                            l_now = i
                    else:
                            answer += 'R'
                            r_now = i
##########
            elif numbers[i] == 5:  # 2,4,6,8
                if r_now == '#':
                    if numbers[l_now] in [2, 4, 6, 8]:
                        answer += 'L'
                        l_now = i
                elif l_now == '*':
                    if numbers[r_now] in [2, 4, 6, 8]:
                        answer += 'R'
                        r_now = i
                else:
                    if numbers[r_now] in [2, 4, 6, 8] and numbers[l_now] in [2, 4, 6, 8]:
                        if hand == 'right':
                            answer += 'R'
                            r_now = i
                        else:
                            answer += 'L'
                            l_now = i
                    elif numbers[r_now] in [2, 4, 6, 8]:
                        answer += 'R'
                        r_now = i
                    elif numbers[l_now] in [2, 4, 6, 8]:
                        answer += 'L'
                        l_now = i
            elif numbers[i] == 8: # 5,7,9,0
                if r_now == '#':
                    if numbers[l_now] in [5, 7, 9, 0]:
                        answer += 'L'
                        l_now = i
                elif l_now == '*':
                    if numbers[r_now] in [5, 7, 9, 0]:
                        answer += 'R'
                        r_now = i
                else:
                    if numbers[r_now] in [5, 7, 9, 0] and numbers[l_now] in [5, 7, 9, 0]:
                        if hand == 'right':
                            answer += 'R'
                            r_now = i
                        else:
                            answer += 'L'
                            l_now = i
                    elif numbers[r_now] in [5, 7, 9, 0]:
                        answer += 'R'
                        r_now = i
                    elif numbers[l_now] in [5, 7, 9, 0]:
                        answer += 'L'
                        l_now = i
            elif numbers[i] == 0: # 8, '*', '#',5,2
                if r_now == '#':
                        answer += 'R'
                        r_now = i
                elif l_now == '*':
                        answer += 'L'
                        l_now = i
                else:
                    if numbers[r_now] in [8, '*', '#'] and numbers[l_now] in [8, '*', '#']:
                        if hand == 'right':
                            answer += 'R'
                            r_now = i
                        else:
                            answer += 'L'
                            l_now = i
                    elif numbers[r_now] in [8, '*', '#']:
                        answer += 'R'
                        r_now = i
                    elif numbers[l_now] in [8, '*', '#']:
                        answer += 'L'
                        l_now = i
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],'left'))