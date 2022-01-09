t=int(input())

p_list=[0,1,1]
for i in range(2,t):
    a=p_list[i]+p_list[i-1]
    p_list.append(a)
print(p_list[t])