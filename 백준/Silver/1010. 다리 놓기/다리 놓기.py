import math
n=int(input())
for x in range(n):
    a,b=map(int,input().split())
    print(math.comb(b,a))