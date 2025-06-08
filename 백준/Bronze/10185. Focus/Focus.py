t=int(input())
for x in range(t):
    a,b=map(int,input().split());
    print(f"f = {round(a*b/(a+b),1):.1f}")