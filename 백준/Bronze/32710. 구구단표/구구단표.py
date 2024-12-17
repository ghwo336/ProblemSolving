s=set()
for x in range(1,10):
    for y in range(1,10):
        s.add(x*y)


n=int(input())
if n in s:
    print(1)
else:
    print(0)