dap=0
n=int(input())
for x in range(1,n+1):
    for y in str(x):
        if y=='3' or y=='6' or y=='9':
            dap+=1
print(dap)