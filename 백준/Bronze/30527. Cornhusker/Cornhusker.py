li=list(map(int,input().split()))
n,kwf=map(int,input().split())
dap=0
for x in range(0,10,2):
    dap+=li[x]*li[x+1]
print(int((dap//5)*n//kwf))