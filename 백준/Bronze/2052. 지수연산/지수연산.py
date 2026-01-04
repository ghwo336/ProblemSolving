n=int(input())
f=5**n
lf=len(str(f))
dap='0.'
dap+=('0'*(n-lf))
dap+=str(f)
print(dap)