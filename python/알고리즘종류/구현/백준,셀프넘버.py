number_set=set(range(1,10000)) # 1 ~ 10000까지 모든 수 set
remove_set=set() # 생성자가 있는 숫자를 담는 set
for num in number_set: # 숫자 하나씩 돌려보며 생성자 있으면 추가
    for i in str(num):
        num+=int(i)
    remove_set.add(num) 

self_number = number_set-remove_set # 모든 수 - 생상자 있는 수 = 생성자 없는 수
for self_num in sorted(self_number): # 내림차순 정렬 후 하나씩 출력
    print(self_num)