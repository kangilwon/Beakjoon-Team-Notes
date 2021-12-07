t = input()
a=list(map(int,input().split()))
a.sort()

grop=0
cnt=0

for i in a:
    cnt+=1
    if cnt >=i:
        grop+=1
        cnt=0
print(grop)
    