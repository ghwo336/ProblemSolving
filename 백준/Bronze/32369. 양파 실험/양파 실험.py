a=1
b=1
N,A,B=map(int,input().split())
for x in range(N):
    a+=A
    b+=B
    if a<b:
        a,b=b,a
    elif a==b:
        b-=1
print(a,b)
