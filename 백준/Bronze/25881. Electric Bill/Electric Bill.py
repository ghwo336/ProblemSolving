n,m=map(int,input().split())
k=int(input())
for x in range(k):
    a=int(input())
    if a<=1000:
        print(a,a*n)
    else:
        print(a,1000*n+(a-1000)*m)