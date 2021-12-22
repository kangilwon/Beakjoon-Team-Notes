n, k = map(int, input().split())

a = input()
b = input()
a = ' '.join(list(a)).split()
b = ' '.join(list(b)).split()
a = list(map(int, a))
b = list(map(int, b))
a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
print(sum(a))

# 동빈나 알고리즘 #
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))
