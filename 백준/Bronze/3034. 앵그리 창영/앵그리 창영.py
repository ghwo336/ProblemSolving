t,a,b=map(int,input().split())
f=a**2+b**2
for x in range(t):
    q=int(input())
    if f<q**2:
        print("NE")
    else:
        print("DA")