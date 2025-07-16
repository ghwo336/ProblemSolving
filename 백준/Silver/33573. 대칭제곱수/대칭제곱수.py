t=int(input())
for x in range(t):
    a=input()
    b=a[::-1]
    a=int(a)
    b=int(b)
    if (int(a**0.5)**2==a) and (int(b**0.5)**2==b):
        print("YES")
    else:
        print("NO")