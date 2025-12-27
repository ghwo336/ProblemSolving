n=int(input())
dap=0
for _ in range(n):
    s,c,a,r=map(int,input().split())
    if s>=1000 or c>=1600 or a>=1500 or 0<=r<=30:
        dap+=1
print(dap)