def dfs(M):
    global u
    if len(u)==M:
        li.append(int(u))
        return
    for x in range(0,10):
        if u:
            if u[-1]>str(x):
                u+=str(x)
                dfs(M)
                u=u[0:len(u)-1]
        else:
            u+=str(x)
            dfs(M)
            u=u[0:len(u)-1]

u=''
li=[]
for x in range(1,11):
    dfs(x)
n=int(input())
if n<len(li):
    print(li[n])
else:
    print(-1)