t= int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    pa=a+d*b
    np=b*c
    if pa>np:
        print('do not parallelize')
    elif pa<np:
        print('parallelize')
    else:
        print('does not matter')