from collections import deque
n,m,r,c=map(int,input().split())
room=deque()
conveniences=[]
graph=[[20000000 for _ in range(m+1)] for _ in range(n+1)]
for _ in range(r):
    x,y,z=map(int,input().split())
    room.append((x,y,z,0))


for _ in range(c):
    x,y=map(int,input().split())
    conveniences.append((x,y))

while room:
    x,y,value,distance=room.popleft()
    if x+1<=n and graph[x+1][y]>value*(distance+1):
        room.append((x+1,y,value,distance+1))
        graph[x+1][y]=value*(distance+1)
    if x-1>0 and graph[x-1][y]>value*(distance+1):
        room.append((x-1,y,value,distance+1))
        graph[x-1][y]=value*(distance+1)
    if y+1<=m and graph[x][y+1]>value*(distance+1):
        room.append((x,y+1,value,distance+1))
        graph[x][y+1]=value*(distance+1)
    if y-1>0 and graph[x][y-1]>value*(distance+1):
        room.append((x,y-1,value,distance+1))
        graph[x][y-1]=value*(distance+1)

dap=2000000000000000000
for convenience in conveniences:
    dap=min(dap,graph[convenience[0]][convenience[1]])
print(dap)

    
    


    

