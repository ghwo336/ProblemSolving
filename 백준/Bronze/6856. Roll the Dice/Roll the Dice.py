a=int(input())
b=int(input())
dap=0
for x in range(1,a+1):
    for y in range(1,b+1):
        if x+y==10:
            dap+=1
if dap!=1:
    print(f'There are {dap} ways to get the sum 10.')
else:
    print(f'There is {dap} way to get the sum 10.')