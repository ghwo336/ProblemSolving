p1=0
p2=0
n=int(input())
for round in range(n):
    a,b=map(int,input().split())
    if a>b:
        p1+=(a+b)
    elif a<b:
        p2+=(a+b)
    else:
        p1+=a
        p2+=b
print(p1,p2)