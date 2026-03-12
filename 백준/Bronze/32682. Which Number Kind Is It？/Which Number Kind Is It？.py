import sys
input=sys.stdin.readline
t=int(input())
for x in range(t):
    a=int(input())
    dap=''
    if a%2==1:
        dap+='O'
    if int(a**0.5)**2==a:
        dap+='S'
    if dap:
        print(dap)
    else:
        print('EMPTY')