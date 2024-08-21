n,m,k=map(int,input().split())
o1=m
x1=n-m
o2=k
x2=n-k
print(min(o1,o2)+min(x1,x2))