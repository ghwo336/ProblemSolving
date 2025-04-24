while(True):
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    c=0
    for x in range(1000001):
        if x**b>=a:
            c=x
            break
    if abs(c**b-a)<=abs((c-1)**b-a):
        print(c)
    else:
        print(c-1)
        