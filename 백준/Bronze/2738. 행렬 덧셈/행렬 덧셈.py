N,M=map(int,input().split())
li1=[]
dap=[[0 for _ in range(M)] for _ in range(N)]
for x in range(N):
    li=list(map(int,input().split()))
    li1.append(li)
li2=[]
for x in range(N):
    li=list(map(int,input().split()))
    li2.append(li)
for x in range(N):
    for y in range(M):
        dap[x][y]=li1[x][y]+li2[x][y]
for x in dap:
    print(*x)