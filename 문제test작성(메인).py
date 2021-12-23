a = input().upper()
del_a = list(set(a))  # 입력받은 문자열에서 중복값을 제거

a_cnt = []
for x in del_a :
    cnt = a.count(x)
    a_cnt.append(cnt)  # count 숫자를 리스트에 append

if a_cnt.count(max(a_cnt)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_value = a_cnt.index(max(a_cnt))  # count 숫자 최대값 인덱스(위치)
    print(del_a[max_value])