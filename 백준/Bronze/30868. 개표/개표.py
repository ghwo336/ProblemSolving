t=int(input())
for x in range(t):
    p=int(input())
    a=p//5
    b=p%5
    for _ in range(a):
        print("++++",end=" ")
    print("|"*b)