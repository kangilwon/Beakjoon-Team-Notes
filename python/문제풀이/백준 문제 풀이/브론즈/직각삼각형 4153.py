a=list(map(int,input().split()))
a_max=a.pop(a.index(max(a)))
while sum(a,a_max)!=0:

    if a[0]**2+a[1]**2==a_max**2:
        print('right')
    else:
        print('wrong')

    a=list(map(int,input().split()))
    a_max=a.pop(a.index(max(a)))