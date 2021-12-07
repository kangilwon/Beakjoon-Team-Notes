a=int(input())
b=int(input())
z=[]
for num in range(a,b+1):
    error=0
    if num > 1:
        for i in range(2, num):
            if num%i==0:
                error+=1
                break
        if error==0:
            z.append(num)

if len(z)>0 :
    print(sum(z))
    print(min(z))
else:
    print('-1')