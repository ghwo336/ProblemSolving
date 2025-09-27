n=int(input())
for x in range(n):
    a,b=map(int,input().split())
    print(a,b)
    print(b+(a-1)*(b-2))