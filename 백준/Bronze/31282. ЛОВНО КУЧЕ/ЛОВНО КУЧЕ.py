n,m,k=map(int,input().split())
d=k-m
if n%d==0:
    print(n//d)
else:
    print(n//d+1)