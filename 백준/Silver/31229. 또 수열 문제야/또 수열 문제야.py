che=[True for _ in range(10000001)]
for x in range(2,10000001):
    if che[x]:
        for y in range(2*x,1000001,x):
            che[y]=False
want=[]
n=int(input())
for x in range(1,1000001):
    if che[x]:
        want.append(x)
    if len(want)==n:
        break
print(*want)