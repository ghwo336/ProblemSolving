while True:
    n=int(input())
    if n==0:
        break
    li=[]
    for x in range(n):
        a,b=input().split()
        b=float(b)
        li.append([b,x,a])
    li.sort()
    p=li[-1][0]
    for x in li:
        if x[0]==p:
            print(x[2],end=" ")
    print("")