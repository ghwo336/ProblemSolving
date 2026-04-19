#31789
n=int(input())
x,s=map(int,input().split())
li=[]
for _ in range(n):
    a,b=map(int,input().split())
    li.append((a,b))

fiv=0
for i in li:
    if i[0]<=x and i[1]>s:
        fiv=1
if fiv:
    print('YES')
else:
    print('NO')