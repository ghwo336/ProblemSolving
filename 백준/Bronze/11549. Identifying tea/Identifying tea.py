a=int(input())
li=list(map(int,input().split()))
dap=0
for x in li:
    if x==a:
        dap+=1
print(dap)