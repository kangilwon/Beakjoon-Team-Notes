'''
A_i = i번째 식량창고까지의 최적의 해(얻을 수 있는 식량의 최댓값)
k_i = i번째 식량창고에 있는 식량의 양
점화식 : A_i = max(A_i-1,A_i-2 + K_i)
    한 칸 이상 떨어진 식량창고는 항상 털 수 있으므로(i - 3)번째 이하는 고려할 필요가 없다.
'''

# 정수 n 입력 받기
n = int(input())
# 모든 식량 정보 입력 받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 'DP 테이블'초기화
d = [0]*100

# 다이나믹 프로그래밍 진행(보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# 계산된 결과 출력
print(d[n - 1])
