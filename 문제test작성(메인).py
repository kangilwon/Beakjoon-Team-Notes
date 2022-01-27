a,b=map(int,input().split())
c=[]
for i in range(b):
    c.append(int(str(a*i)[::-1]))

print(max(c))


