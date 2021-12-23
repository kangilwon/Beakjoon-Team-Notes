# 값이 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n,m=map(int,input().split())
# 배열 선언
array=list(map(int,input().split()))

# 값이 m인 데이터 개수 출력
if m in array:
    print(count_by_range(array,m,m))
else:
    print('-1')
