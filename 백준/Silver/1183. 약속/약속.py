li=[]
n=int(input())
for x in range(n):
    a,b=map(int,input().split())
    li.append(b-a)
li.sort()
dap=1
if len(li)%2==0:
    fiv=len(li)//2-1
    dap=li[fiv+1]-li[fiv]+1
print(dap)