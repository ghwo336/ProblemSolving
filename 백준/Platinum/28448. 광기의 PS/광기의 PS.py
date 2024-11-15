N,L=map(int,input().split())
li=[]
result=0
f=0
for x in range(N):
    K,T=map(int,input().split())
    if T>5:
        li.append([K,T])
    else:
        result+=T        
li.sort()
li.reverse()
if len(li)!=0:
    for x in range(len(li)-1):
        if f+li[x][0]*li[x][1]<=L:
            f+=li[x][0]*li[x][1]-5*li[x][0]
            result+=li[x][1] 
        else:
            result+=(f+li[x][0]*li[x][1]-L)+li[x][1]
            f=L-5*li[x][0]
            
    if f+li[-1][0]*li[-1][1]>L:
        result+=f+li[-1][0]*li[-1][1]-L+li[-1][1]
    else:
        result+=li[-1][1]
    print(result)
else:
    print(result)