N=int(input())
li=[]
for x in range(5000000):
    if x%2==0:
        li.append(x//2)
    else:
        li.append(x//2+1)
for x in range(1,500000):
    li[x]=li[x]+li[x-1]

for x in range(N):
    a,b=map(int,input().split())
    cha=b-a
    for y in range(int(cha**0.5)*2-1,500000):
        if li[y]>=cha:
            print(y)
            break