n=int(input())
li=list(map(int,input().split()))
li2=list(map(int,input().split()))
dap1=0
dap2=0
for x in range(n):
    dap1+=li[x]
    if not li2[x]:
        dap2+=li[x]
print(dap1)
print(dap2)