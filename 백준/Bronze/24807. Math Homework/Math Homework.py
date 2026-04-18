#24807
b,c,d,l=map(int,input().split())
fiv=1
for x in range(l+1):
    for y in range(l+1):
        re=l-b*x-c*y
        if re<0:
            continue
        if (re)%d==0:
            print(x,y,re//d)
            fiv=0
if fiv:
    print('impossible')