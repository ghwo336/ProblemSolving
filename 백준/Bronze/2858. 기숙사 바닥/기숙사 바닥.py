b,r=map(int,input().split())
f=b+r

for x in range(1,f+1):
    if f%x==0:
        n=x
        m=f//x
        if 2*n+2*m-4==b:
            print(m,n)
            break
    