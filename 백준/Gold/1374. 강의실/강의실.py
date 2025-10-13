import heapq
classroom=0
left=0
n=int(input())
heap=[]
for x in range(n):
    cn,start,end=map(int,input().split())
    heapq.heappush(heap,(start,end))
while heap:
    ns,ne=heapq.heappop(heap)
    if ns==ne:
        left+=1
    else:
        if left>0:
            left-=1
            heapq.heappush(heap,(ne,ne))
        else:
            classroom+=1
            heapq.heappush(heap,(ne,ne))

print(classroom)