from collections import Counter

mylist = input().strip()
dic = dict(Counter(mylist))

values = [i for i in dic.values()]
values = sorted(values, reverse=True)

big = values[0]

result = [i for i, k in dic.items() if big == k]
result = ''.join(sorted(result))
print(result)