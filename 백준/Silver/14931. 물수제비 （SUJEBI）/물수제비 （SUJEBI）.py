n=int(input())
li=[0]+list(map(int,input().split()))
max=-10000000000000000000000000000000
dap=0
for p in range(1,n+1):
    now=p
    hubo=0
    while now<=n:
        hubo+=li[now]
        now+=p
    if max<hubo:
        max=hubo
        dap=p
if max>0:
    print(dap,max)
else:
    print('0 0')
        