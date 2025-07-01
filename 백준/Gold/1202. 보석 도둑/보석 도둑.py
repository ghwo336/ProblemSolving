import heapq
n,k=map(int,input().split())
bags=[]
diamonds=[]
for x in range(n):
    diamonds.append(list(map(int,input().split())))
for y in range(k):
    bags.append(list(map(int,input().split())))

hq=[]
diamonds.sort()
bags.sort()
now=0
dap=0
for bag in bags:
    while True:
        if now==n:
            if hq:
                dap+=-(heapq.heappop(hq))
            break
                
            break
        massm,value=diamonds[now]
        if bag[0]>=massm:
            heapq.heappush(hq,-value)
            now+=1
        else:
            if hq:
                dap+=-(heapq.heappop(hq))
            break

print(dap)
                
    
    
    