t1,m1,t2,m2=map(int,input().split())
s1=60*t1+m1
s2=60*t2+m2
if s1>s2:
    s2+=24*60
dap=s2-s1
print(dap,dap//30)