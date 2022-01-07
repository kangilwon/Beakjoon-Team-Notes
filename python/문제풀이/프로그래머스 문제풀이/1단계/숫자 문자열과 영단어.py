def solution(s):
    num_str = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
               '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}

    for key,value in num_str.items():
        if value in s:
            s = s.replace(value, key)

    answer = int(s)

    return answer

print(solution(input()))