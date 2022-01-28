a,b=map(int,input().split())
c=[]
for i in range(1,b+1):
    c.append(int(str(a*i)[::-1]))

print(c,max(c))


