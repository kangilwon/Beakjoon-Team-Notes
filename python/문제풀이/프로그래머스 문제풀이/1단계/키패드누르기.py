def solution(numbers, hand):
    answer = ''
    r_now = 10
    l_now = 12

    for i in numbers:
        if i in [3, 6, 9]:
            answer += 'R'
            r_now = i
        elif i in [1, 4, 7]:
            answer += 'L'
            l_now = i
        else:
            i = 11 if i == 0 else i
            l_point = abs(i-l_now)
            r_point = abs(i-r_now)

            if sum(divmod(l_point, 3)) > sum(divmod(r_point, 3)):
                answer += 'R'
                r_now = i
            elif sum(divmod(l_point, 3)) < sum(divmod(r_point, 3)):
                answer += 'L'
                l_now = i
            else:
                if hand == 'left':
                    answer += 'L'
                    l_now = i
                else:
                    answer += 'R'
                    r_now = i
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],'left'))