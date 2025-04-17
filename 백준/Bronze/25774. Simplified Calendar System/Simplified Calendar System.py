a,b,c,d=map(int,input().split())
e,f,g=map(int,input().split())
dap=(e+30*f+360*g)-(a+30*b+360*c)+d
if dap%7==0:
    print(7)
else:
    print(dap%7)