n=int(input())
li=list(map(int,input().split()))
dap=0
for x in li:
    dap+=(x//2)
    if x%2==1:
        dap+=1
print(dap)
    