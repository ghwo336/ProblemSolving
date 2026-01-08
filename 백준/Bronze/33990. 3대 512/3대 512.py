n=int(input())
li=[]
for x in range(n):
    a,b,c=map(int,input().split())
    if a+b+c>=512:
        li.append(a+b+c)
if li:
    li.sort()
    print(li[0])
else:
    print(-1)