n=int(input())
li=list(input().split())
for x in range(n):
    li[x]+='DORO'
for x in range(n):
    print(li[x],end=' ')