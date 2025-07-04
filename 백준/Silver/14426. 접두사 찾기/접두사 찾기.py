n,m=map(int,input().split())
s=set()
for x in range(n):
    a=input()
    k=''
    for y in a:
        k+=y
        s.add(k)
dap=0
for y in range(m):
    a=input()
    if a in s:
        dap+=1
print(dap)