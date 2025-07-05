n,m=map(int,input().split())
li=[]
for x in range(n):
    a=input()
    li.append(a)
di=dict()
for x in li:
    if x not in di:
        di[x]=1
    else:
        di[x]+=1
k=int(input())
dap=0
for x in di:
    num0=0
    for y in x:
        if y=='0':
            num0+=1
    if num0<=k and k%2==num0%2:
        dap=max(dap,di[x])
print(dap)