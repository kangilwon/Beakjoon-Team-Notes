def solution(new_id):
    answer=''

    # 1단계 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id=new_id.lower()

    # 2단계 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    for i in new_id:
        if i.isalnum() or i in ['-', '_', '.']:
            answer += i

    # 3단계 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'

    if answer[-1] == '.':
        answer = answer[:-1]

    # 5단계 빈 문자열이라면, answer에 "a"를 대입합니다.
    if answer == '':
        answer = 'a'

    # 6단계 길이가 16자 이상이면, answer의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
        #만약 제거 후 마침표(.)가 answer의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계 길이가 2자 이하라면, answer의 마지막 문자를 answer의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(answer) < 3:
        answer += answer[-1]


    return answer
    
solution(input())