li=list(map(int,input().split()))
x,y,r=map(int,input().split())
pandan=1
for z in range(4):
    if li[z]==x:
        print(z+1)
        pandan=0
if pandan:
    print(0)
    