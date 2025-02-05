n=int(input())
k=int(input())
che=[True for _ in range(100001)]
for x in range(2,100000):
    if che[x]:
        for y in range(2*x,100001,x):
            che[y]=False
sosu=[]
for x in range(k+1,100001):
    if che[x]:
        sosu.append(x)
che=[True for _ in range(n+1)]
che[0]=False

for x in sosu:
    for y in range(x,n+1,x):
        che[y]=False
dap=0
for x in che:
    if x:
        dap+=1
print(dap)
    