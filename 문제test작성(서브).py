a = int(input())
this='not found'
for i in range(4):
    b = a*int(input())
    if b**0.5==int(b**0.5):
        this='found'
        break

print(this)


        