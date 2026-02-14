
dap=0
n=int(input())
a=input()
for x in a:
    dap+=(ord(x)-96)
if len(a)>n:
    print('Impossible')
else:
    print(dap)