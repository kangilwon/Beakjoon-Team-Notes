def solution(new_id):
    # answer=list(answer)
    # 문자제약(알파벳 소문자, 숫자, . - _)
    as_num=48 # 아스키코드 숫자 0
    str_o=list(range(97,123)) # 아스키코드 알파벳 소문자 a~z
    str_o.append(45) # 아스키코드 - -
    str_o.append(46) # 아스키코드 - .
    str_o.append(95) # 아스키코드 - _

    # int 형태의 리스트의 value를 아스키 코드로 변환한다.
    for i in range(len(str_o)):
        str_o[i]=chr(str_o[i])
    # 숫자의 아스키코드 0 ~ 9 까지
    for i in range(10):
        str_o.append(chr(as_num))
        as_num+=1
        
    answer = str_o

    # for i in (list(answer)):
    #     if i not in str_o:
    #         answer=answer-i
    

    return answer
    
id=input().lower
print(solution(id))
