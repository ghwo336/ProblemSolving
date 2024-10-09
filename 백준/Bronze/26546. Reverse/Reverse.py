T=int(input())
for _ in range(T):
    s,a,b=input().split()
    a=int(a)
    b=int(b)
    for x in range(len(s)):
        if not( x>=a and x<b):
            print(s[x], end= "")
    print("")