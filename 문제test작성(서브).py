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
m,n=map(int,input().split())

for i in primes(n):
    if i>=m:
        print(i)