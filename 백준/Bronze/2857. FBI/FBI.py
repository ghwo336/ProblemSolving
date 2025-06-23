dap=[]
for x in range(5):
    a=input()
    if "FBI" in a:
        dap.append(x+1)
if dap:
    print(*dap)
else:
    print("HE GOT AWAY!")