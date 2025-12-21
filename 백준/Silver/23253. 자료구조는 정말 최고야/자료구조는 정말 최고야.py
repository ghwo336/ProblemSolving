n,m=map(int,input().split())
fiv=True
for x in range(m):
    a=int(input())
    li=list(map(int,input().split()))
    for x in range(a-1):
        if li[x]<li[x+1]:
            fiv=False
if fiv:
    print('Yes')
else:
    print('No')