n=int(input())
li=list(map(int,input().split()))
dap=sum(li)+8*(n-1)
print(dap//24,dap%24)