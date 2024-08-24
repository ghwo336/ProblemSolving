N=int(input())
for x in range(N):
    a,b=map(int,input().split())
    print(a+b//4-b//7)