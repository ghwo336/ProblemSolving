def fac(num):
    if num==0:
        return 1
    return num*fac(num-1)
    

while(True):
    a=input()
    if a=='0':
        break
    dap=0
    for x in range(len(a)):
        dap+=(fac(len(a)-x)*int(a[x]))
    print(dap)
        