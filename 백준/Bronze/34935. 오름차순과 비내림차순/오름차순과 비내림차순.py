n=int(input())
li=list(map(int,input().split()))
f=1
for x in range(n-1):
    if li[x]>=li[x+1]:
        f=0
print(f)