a,b=map(int,input().split())
for x in range(1,min(a,b)+1):
    if a%x==0 and b%x==0:
        print(x,a//x,b//x)