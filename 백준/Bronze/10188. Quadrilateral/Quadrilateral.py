t=int(input())
for x in range(t):
    a,b=map(int,input().split())
    for _ in range(b):
        print('X'*a)
    if x!=t-1:
        print('')