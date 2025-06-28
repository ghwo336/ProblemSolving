n=int(input())
start=0
end=n-1
li=list(map(int,input().split()))
dap=2000000000000000000
while(start<end):
    if abs(li[start]+li[end])<abs(dap):
        dap=li[start]+li[end]
    if li[start]+li[end]>0:
        end-=1
    elif li[start]+li[end]==0:
        dap=0
        break
    else:
        start+=1
print(dap)
        