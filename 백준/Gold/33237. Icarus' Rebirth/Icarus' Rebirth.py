from heapq import heappop,heappush
import sys
input = sys.stdin.readline
a=input().rstrip()
l=len(a)
di=dict()
for x in range(l):
    if a[x] not in di:
        di[a[x]]=[x]
    else:
        di[a[x]].append(x)
visit={0}
heap=[]
heappush(heap,(0,0))
dap=-1
near=[[] for _ in range(l)]
for x in range(l):
    if x>=1:
        near[x].append(x-1)
    if x<l-1:
        near[x].append(x+1)
for x in di:
    l2=len(di[x])
    for y in range(1,l2):
        near[di[x][y]].append(di[x][y-1])
    for y in range(l2-1):
        near[di[x][y]].append(di[x][y+1])
for x in range(l):
    near[x]=list(set(near[x]))

while heap:
    num,now=heappop(heap)
    
    if now==l-1:
        dap=num
        break
    for x in near[now]:
        if x not in visit:
            visit.add(x)
            heappush(heap,(num+1,x))
                
print(dap)
