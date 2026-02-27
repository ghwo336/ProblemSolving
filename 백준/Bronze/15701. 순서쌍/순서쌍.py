a=int(input())
dap=0
for x in range(1,int(a**0.5)+1):
    if a%x==0:
        dap+=2
    if a==x*x:
        dap-=1
print(dap)
    