d=''
c=list(map(int,input().split()))
c.sort()
for i in range(len(c)):
    d+=str(c[i])+' '
print(d[:-1])    