a=input()[:5]
n=int(input())
dap=0
for x in range(n):
    b=input()[:5]
    if a==b:
        dap+=1
print(dap)