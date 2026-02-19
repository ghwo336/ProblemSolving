n=int(input())
a=input()
b=input()
dap=0
for x in range(n):
    if a[x]!=b[x]:
        dap+=1
print(dap)