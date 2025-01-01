n=int(input())
li1=list(map(int,input().split()))
dap=0
li2=list(map(int,input().split()))

for x in range(n):
    if li2[x]>=li1[x]:
        dap+=1
print(dap)