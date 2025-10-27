n=int(input())
dap=0
for x in range(1,n//3+1):
    for y in range(n):
        first=x
        second=x+y
        third=n-(first+second)
        if second<=third and first+second>third:
            dap+=1
        if second>third:
            break
print(dap)