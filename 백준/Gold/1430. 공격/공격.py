from collections import  deque
n,r,d,x,y=map(int,input().split())
tops=[]
q=deque()
q.append([0,x,y])
visit=set()
dap=0.0

for _ in range(n):
    px,py=map(int,input().split())
    tops.append([px,py])
while q:
    num,nowx,nowy=q.popleft()
    for top in tops:
        topx=top[0]
        topy=top[1]
        if (nowx-topx)**2+(nowy-topy)**2<=r**2:
            if (topx,topy) not in visit:
                visit.add((topx,topy))
                dap+=d/(2**(num))
                q.append((num+1,topx,topy))
print(dap)
        
        
    


