# 나이트의 현재 위치
input_data=input()
row=int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a'))+1

# 나이트의 이동방향
steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# 8방향으로 이동이 가능한지 확인한다.
result=0
for step in steps:
    # 이동할 위치 확인
    next_row=row+step[0]
    next_column=column+step[1]
    # 해당 위치로 이동이 가능하면 카운트를 증가시킨다.
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        result+=1

print(result)