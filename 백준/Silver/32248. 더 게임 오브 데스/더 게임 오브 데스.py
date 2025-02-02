
n,t=map(int,input().split())
li=[0]+list(map(int,input().split()))
ci=[1]
fiv=-1
while t!=0:
    now=ci[-1]
    if li[now] not in ci:
        t-=1
        ci.append(li[now])
    else:
        t-=1
        fiv=li[now]
        break

if fiv==-1:
    print(ci[-1])
else:
    tap=-1
    for x in range(len(ci)):
        if ci[x]==fiv:
          tap=x
    cilen=len(ci)-tap
    print(ci[tap+t%cilen])
    
