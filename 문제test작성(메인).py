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

# '''
# 파이썬 트라이 캐치? 무한반복 종료 (파이썬 eof)
# while True:
#     try:
#         a,b=map(int,input().split())
#         print(a+b)
#     except:
#         break
# '''

# 유클리드 호제법(최대공약수-gcd,최소공배수-lcm)
'''
import math
print(math.gcd(a,b))
print(math.lcm(a,b))
'''


# 에라토네스의 체(소수문제)
'''
def primes(t):
    sieve = [True] * t  # '에라토네스의 체'초기화 : t개 요소에 True로 설정하여 소수로 간주한다.

    m = int(t ** 0.5)  # t의 최대 약수는 항상 루트(sqrt(t))이하임 따라서 i 는 루트t 까지 검사한다.

    for i in range(2, m+1):
        if sieve[i] == True:  # list sieve의 [i]번째 수가 소수면 i의 배수를 False로 설정한다.
            for j in range(i+i, t, i):  # i를 제외하고 | t 값까지 | i만큼 증가시키며(i의 배수)
                sieve[j] = False
    # i 에 대입한다, 2부터 입력값 t 까지 반복한다, sieve[i]가 True인 수를,
    return [i for i in range(2, t)if sieve[i] == True]
    # 즉, 소수만 sieve에 담아 리스트로 출력한다.
'''

# 리스트(스트링, 인트 혼합)
'''
t=int(input()) # 학생 수
stu_list=[] # 학생들의 리스트

for stu_index in range(t): # 학생 수만큼 반복하며 인덱스값 저장
    stu=input().split() # 학생 이름과 생년월일 입력.
    stu[1:]=map(int,stu[1:]) # 인덱스 1번 부터 int값으로 변환시킴
    stu_list.append(stu) # 변환한 학생정보를 리스트에 저장한다.

# 학생들 리스트를 연,월,일 기준 오름차순 정렬 (나이만음 -> 어림)
stu_list.sort(key=lambda stu:(stu[3],stu[2],stu[1]))

# 제일 뒤가 어린 사람임
print(stu_list[-1][0]) # stu_list의 , [-1] 제일 뒤 , [0] 이름
print(stu_list[0][0]) # stu_list의 , [0] 첫번 째 , [0] 이름
'''