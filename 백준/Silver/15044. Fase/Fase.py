n=int(input())
f=int(input())
li=[0 for _ in range(1001)]
for x in range(n):
    a=int(input())
    li[a]+=1
li.reverse()
dap=0
for x in li:
    if f>0:
        f-=x
        dap+=x
    else:
        break
print(dap)
        