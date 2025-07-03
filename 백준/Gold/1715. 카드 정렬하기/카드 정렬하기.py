import heapq
n=int(input())
li=[]
for x in range(n):
    a=int(input())
    heapq.heappush(li,a)
dap=0
for x in range(n-1):
    a=heapq.heappop(li)
    b=heapq.heappop(li)
    dap+=(a+b)
    heapq.heappush(li,a+b)
print(dap)