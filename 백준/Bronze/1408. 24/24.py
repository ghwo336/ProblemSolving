a,b,c=map(int,input().split(':'))
d,e,f=map(int,input().split(':'))
now = 3600*a + 60*b + c
start = 3600*d + 60*e + f
dap=0
if start>now:
    dap=start-now
else:
    dap=start-now+86400
s=str(dap//3600)
dap%=3600
m=str(dap//60)
dap%=60
dap=str(dap)
if len(s)==1:
    s='0'+s
if len(m)==1:
    m='0'+m
if len(dap)==1:
    dap='0'+dap
print(f'{s}:{m}:{dap}')