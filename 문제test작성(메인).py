t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    cnt=0
    while True:
        if c <= 0:
            c+=a
            break
        cnt+=1
        c-=a
    c *= 100 
    
    
    print(c+cnt)
    
