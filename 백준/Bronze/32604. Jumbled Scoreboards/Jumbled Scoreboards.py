t=int(input())
a=[]
b=[]
for x in range(t):
    c,d=map(int,input().split())
    a.append(c)
    b.append(d)
fiv=True
for x in range(1,t):
    if a[x]<a[x-1]:
        fiv=False
    if b[x]<b[x-1]:
        fiv=False
if fiv:
    print('yes')
else:
    print('no')