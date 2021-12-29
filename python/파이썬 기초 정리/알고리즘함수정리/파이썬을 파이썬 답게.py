# # a, b = map(int, input().strip().split(' '))
# # print(a//b,a%b)
# # # 더 간단하게
# # print(*divmod(a,b))

# # # int를 사용하면  | 특정수 num  |  base n진수  |를 이용하여 간단하게 표현할 수 있다./ 단, 특저 수는 str이어야 한다.
# # int(str(num), base)

# # 좌측정렬 | 우측정렬 | 가운데정렬
# # 파이썬에서는 ljust, center, rjust와 같은 string의 메소드를 사용해 코드를 획기적으로 줄일 수 있습니다.
# s = '가나다라'
# n = 7

# s.ljust(n) # 좌측 정렬
# s.center(n) # 가운데 정렬
# s.rjust(n) # 우측 정렬


# # 파이썬은 이런 데이터를 상수(constants)로 정의해놓았습니다.
# # 더 많은 string 상수를 python documentation(https://docs.python.org/3.4/library/string.html) 에서 확인해보세요.
# import string 

# string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
# string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.digits # 숫자 0123456789


# # 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# # 보통 사람들은 deep copy와 sort 함수를 이용합니다.
# # list1 = [3, 2, 1]
# # list2 = [i for i in list1] # 또는 copy.deepcopy를 사용
# # list2.sort()
# # 파이썬의 sorted를 사용해보세요. 반복문이나, deepcopy 함수를 사용하지 않아도 새로운 정렬된 리스트를 구할 수 있습니다.

# list1 = [3, 2, 1]
# list2 = sorted(list1)


# # 2차원 리스트 뒤집기
# def solution(mylist):
#     answer = [[],[],[]]
#     for i in range(len(mylist)):
#         for j in range(len(mylist[i])):
#             answer[i].append(mylist[j][i])
#     return answer

# print(solution(mylist= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# ## 간단하게  |  참고(https://programmers.co.kr/learn/courses/4008/lessons/13318)
# mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_list = list(map(list, zip(*mylist)))



# # i + (i+1)
# def solution(mylist):
#     answer = []
#     for number1, number2 in zip(mylist, mylist[1:]):
#         answer.append(abs(number1 - number2))
#     return answer
    

# 리스트의 형변환
list1 = ['1', '100', '33']
list2 = list(map(int, list1))
## 응용하면 길이값 반환도 가능하다
list3 = list(map(len, list1))
## 리스트 문자열로
print(''.join(list1))


# itertools.product를 이용하면, for 문을 사용하지 않고도 곱집합을 구할 수 있습니다.

import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))



 # 파이썬의 다양한 기능을 사용하면, for 문을 사용하지 않고도 리스트를 이어 붙일 수 있습니다.

my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))

# 제한적으로 사용 가능한 방법
# 아래의 방법은 각 원소의 길이가 동일한 경우에만 사용 가능합니다.

# 방법 7 - numpy 라이브러리의 flatten 이용
import numpy as np
np.array(my_list).flatten().tolist()
# 예를 들어 다음과 같은 리스트는 편평하게 만들 수 있고

[[1], [2]]
[[1, 2], [2, 3], [4, 5]]
# 다음과 같이 같이 각 원소의 길이가 다른 리스트는 편평하게 만들 수 없습니다.

[['A', 'B'], ['X', 'Y'], ['1']]



# 순열과 조합 - combinations, permutations
## 이번 강의에서는 iterable의 원소로 순열과 조합을 구하는 방법을 배워봅시다.

# itertools.permutation를 이용하면, for문을 사용하지 않고도 순열을 구할 수 있습니다.

import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
# ※ 조합은 itertools.combinations를 사용해서 구할 수 있습니다. 사용법은 permutations와 비슷해요!
'''
import itertools

def solution(mylist):
    answer=list(itertools.permutations(mylist,len(mylist)))
    for i in range(len(answer)):
        answer[i]=list(answer[i])
    answer.sort()
    return answer
'''


## 파이썬의 collections.Counter 클래스를 사용하면 
'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = {}
for number in my_list:
    try:
        answer[number] += 1
    except KeyError:
        answer[number] = 1

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100])  # =  raise KeyError
'''
# 이 코드를 간략하게 만들 수 있습니다.

import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0



## 파이썬의 list comprehension을 사용하면 한 줄 안에 for 문과 if 문을 한 번에 처리할 수 있습니다.

mylist = [3, 2, 6, 7]
answer = [number**2 for number in mylist if number % 2 == 0]




## 파이썬에서는 다음과 같이 한 줄로 두 값을 바꿔치기할 수 있습니다. 

a = 3
b = 'abc'

a, b = b, a # 참 쉽죠?




## 파이썬에서는 파이썬의 bisect.bisect 메소드를 사용하면 이 코드를 간략하게 만들 수 있습니다.

import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))
# 이진 탐색 - 오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘. 검색 속도가 아주 빠르다. 


## 가장 큰 수, inf
# 코딩 테스트 문제 등을 풀다 보면, 최솟값을 저장하는 변수에 아주 큰 값을 할당해야 할 때가 있습니다. 이번 시간에는 이때에 사용하기 좋은 inf에 대해 알아봅시다.
# inf는 어떤 숫자와 비교해도 무조건 크다고 판정됩니다.

min_val = float('inf')
min_val > 10000000000

# inf에는 음수 기호를 붙이는 것도 가능합니다.
max_val = float('-inf')



## 파일을 읽을 때
# 파이썬에서는 파이썬의 with - as 구문을 이용하면 코드를 더 간결하게 짤 수 있습니다. 코드를 아래와 같이 쓰면 다음과 같은 장점이 있습니다.
# 파일을 close 하지 않아도 됩니다: with - as 블록이 종료되면 파일이 자동으로 close 됩니다.
# readlines가 EOF까지만 읽으므로, while 문 안에서 EOF를 체크할 필요가 없습니다.
with open('myfile.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))
# ⨳ with - as 구문은 파일 뿐만 아니라 socket이나 http 등에서도 사용할 수 있습니다.