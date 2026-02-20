n,m=map(int,input().split())
li=[]
for x in range(n):
    li2=list(input())
    li.append(li2)
fiv=0
for x in range(m):
    fiv2=1
    for y in range(n):
        if li[y][x]=='O':
            fiv2=0
    if fiv2:
        fiv=x+1
        break
if fiv:
    print(fiv)
else:
    print("ESCAPE FAILED")
            
            