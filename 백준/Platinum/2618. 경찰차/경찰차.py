import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
dp=[[0 for _ in range(M+1)] for _ in range(M+1)]
car1=[(1,1)]
car2=[(N,N)]
dap=[]
dapli=[]
for x in range(M):
    a,b=map(int,input().split())
    car1.append((a,b))
    car2.append((a,b))
dp[0][1]=abs(car1[0][0]-car1[1][0])+abs(car1[0][1]-car1[1][1])
dp[1][0]=abs(car2[0][0]-car2[1][0])+abs(car2[0][1]-car2[1][1])


for y in range(M+1):
    for x in range(M+1):
        if y!=x and not (x==0 and y==1) and not (y==0 and x==1):
            if y-x==1:
                m=100000000000
                for k in range(y-1):
                    m=min(m,dp[k][x]+abs(car2[k][0]-car2[y][0])+abs(car2[k][1]-car2[y][1]))
                dp[y][x]=m
            elif x-y==1:
                m=100000000000
                for k in range(x-1):
                    m=min(m,dp[y][k]+abs(car1[k][0]-car1[x][0])+abs(car1[k][1]-car1[x][1]))
                dp[y][x]=m
            elif y>x:
                dp[y][x]=dp[y-1][x]+abs(car2[y][0]-car2[y-1][0])+abs(car2[y][1]-car2[y-1][1])
            elif y<x:
                dp[y][x]=dp[y][x-1]+abs(car1[x][0]-car1[x-1][0])+abs(car1[x][1]-car1[x-1][1])
            if y==M or x==M:
                dapli.append(dp[y][x])
                dap.append((x,y))
au=min(dapli)

print(au)
hn=[]
for x in range(len(dap)):
    if dapli[x]==au:
        hn.append(dap[x])
        break
x=hn[0][0]
y=hn[0][1]
realdap=[]
realdap.append((x,y))
for _ in range(M):
    if (x==0 and y==1) or (x==1 and y==0):
        break
    elif y-x==1:
        for k in range(y-1):
            if dp[y][x]==dp[k][x]+abs(car2[k][0]-car2[y][0])+abs(car2[k][1]-car2[y][1]) :
                y=k
                realdap.append((x,y))
                break          
    elif x-y==1:
        for k in range(x-1):
            if dp[y][x]==dp[y][k]+abs(car1[k][0]-car1[x][0])+abs(car1[k][1]-car1[x][1]):
                x=k
                realdap.append((x,y))
                break          
    elif x>y:
        x-=1
        realdap.append((x,y))
    elif x<y:
        y-=1
        realdap.append((x,y))
fiv=[0,0]
realdap.reverse()

for x in realdap:
    if fiv[0]!=x[0]:
        print('1')
        fiv[0]=x[0]
    else:
        print('2')
        fiv[1]=x[1]
            