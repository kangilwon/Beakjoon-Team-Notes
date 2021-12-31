'''
이 문제의 기본 아이디어는 "가장 긴 증가하는 부분 수열(Longest Lncreasing Subsequence, LIS)"로 알려진 전형적인 다이나믹 프로그래밍 문제와 같다.
EX
    하나의 수열 array={4,2,5,8,4,11,15}이 있다.
        이 수열의 '가장 긴 증가하는 부분 수열'은 {4,5,8,11,15}이다
    본 문제는 '가장 긴 감소하는 부분 수열을 찾는 문제로 치환'할 수 있으므로, LIS알고리즘을 조금 수정하여 정답을 도출할 수 있다.

    가장 긴 증가하는 부분 수열(LIS)알고리즘
        D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
        점화식 : 모든 0 <= j < i 에 대하여, D[i] = max(D[i], D[j] + 1) if array[j] < arrat[i]

    가장 먼저 입력 받은 병사 정보의 순서를 뒤집는다.
    가장 긴 증가하는 부분 수열 알고리즘을 수행하여 정답을 도출하낟.
'''

n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 치환한다.
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP테이블 초기화
dp = [1]*n

# 가장 긴 증가하는 부분 수열 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

# 열외해야 하는 벙사의 최소 수를 출력한다.
print(n - max(dp))
