n = int(input()) # 배열 크기
move=list(map(str,input().split()))

x, y = 1, 1 # 초기값

r=d=1
l=u=-1

for i in range(1, n+1):
    for j in range(1, n+1):
        print(i, j, end='  ')
    print()

for i in move:
    if i == 'r':
        if y==n:
            continue
        else:
            y+=r
    elif i == 'l':
        if x==1:
            continue
        else:
            x+=l
    elif i == 'u':
        if x==1:
            continue
        else:
            y += u
    elif i == 'd':
        if x==n:
            continue
        else:
            x += d
    

print(x, y)

# 동빈나
'''
n = int(input()) # n*n 배열 크기
x, y = 1, 1 # 초기값
plans=input().split() #이동계획

#     L  R  U  D 에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types=['L','R','U','D']

# 이동 계획을 하나씩 확인한다.
for plan in plans:
    # 이동 후 좌표를 구한다.
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간을 벗어나는 경우 무시한다.
    if nx < 0 or ny < 1 or nx > n or ny > n:
        continue

    # 이동 수행
    x, y = nx, ny

print(x, y)
'''