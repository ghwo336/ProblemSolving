a=int(input())
dap=0
s=input()
for x in s:
    dap+=ord(x)
print(dap-64*a)