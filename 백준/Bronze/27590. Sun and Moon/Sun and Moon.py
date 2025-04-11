a,b=map(int,input().split())
c,d=map(int,input().split())
s=set()
t1=-a+b
while t1<=5000:
    s.add(t1)
    t1+=b
t2=-c+d
while t2<=5000:
    if t2 in s:
        print(t2)
        break
    t2+=d



    