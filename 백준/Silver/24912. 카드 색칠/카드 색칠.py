n=int(input())
li=list(map(int,input().split()))
if n==1:
    if li[0]==0:
        print(1)
    else:
        print(*li)
else:
    for x in range(n):
        if li[x]==0:
            if x==0:
                if li[x+1]==0:
                    li[x]=1
                elif li[x+1]==1:
                    li[x]=2
                elif li[x+1]==2:
                    li[x]=3
                elif li[x+1]==3:
                    li[x]=1
            elif x==n-1:
                if li[x-1]==1:
                    li[x]=2
                elif li[x-1]==2:
                    li[x]=3
                elif li[x-1]==3:
                    li[x]=1
            else:
                s={1,2,3}
                s.discard(li[x-1])
                s.discard(li[x+1])
                s=list(s)
                li[x]=s[0]
    fiv=0
    for x in range(n-1):
        if li[x]==li[x+1]:
            fiv=1
    for x in range(n):
        if li[x]==0:
            fiv=1
    if fiv:
        print(-1)
    else:
        print(*li)

            