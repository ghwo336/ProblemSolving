t=0
p=0
n,m=map(int,input().split())
li=list(map(int,input().split()))
for x in li:
    if p+x<=m:
        print(t)
        p+=x
    else:
        p=x
        t+=1
        print(t)
        