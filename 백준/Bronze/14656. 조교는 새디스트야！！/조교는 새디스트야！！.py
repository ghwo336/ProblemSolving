n=int(input())
li=list(map(int,input().split()))
dap=0
for x in range(n):
    if li[x]!=x+1:
        dap+=1
print(dap)