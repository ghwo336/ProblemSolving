n,k=map(int,input().split())
if k==1 and n==2:
    print('1 2')
elif n!=1:
    print(-1)
else:
    print(*([1]*k))