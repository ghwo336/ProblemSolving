n=int(input())
dap=0
for _ in range(n):
    a=input()
    for x in range(len(a)-1):
        if a[x]=='0'and a[x+1]=='1':
            dap+=1
            break
        elif a[x]=='O' and a[x+1]=='I':
            dap+=1
            break
print(dap)