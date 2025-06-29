n,m= map(int,input().split())
li=[]
for x in range(n):
    li.append(int(input()))
start=0
end=0
li.sort()
dap=10000000000000000000000000000000000
while (start<=end and end<n):
    if li[end]-li[start]>=m:
        cha=li[end]-li[start]
        dap=min(dap,cha)
        start+=1
    else:
        end+=1
print(dap)