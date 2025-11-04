n,d=map(int,input().split())
li=[]
for x in range(n):
    p,v=map(int,input().split())
    li.append([p,v])
li.sort()
start=0
end=0
dap=0
now=0
while end<n:
    if li[end][0]-li[start][0]<d:
        now+=li[end][1]
        end+=1
    else:
        start+=1
        now-=li[start-1][1]
    dap=max(dap,now)
print(dap)
    