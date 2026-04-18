#10419
t=int(input())
for _ in range(t):
    a=int(input())
    for x in range(a+1):
        if x**2+x>a:
            print(x-1)
            break
    