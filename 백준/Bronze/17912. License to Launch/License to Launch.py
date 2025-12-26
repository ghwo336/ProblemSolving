n=int(input())
li=list(map(int,input().split()))
s=min(li)
for x in range(n):
    if li[x]==s:
        print(x)
        break