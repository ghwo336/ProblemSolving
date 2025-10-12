n=int(input())
dap=[]
def bt(i):
    dap.append(int(i))
    for j in range(int(i[-1])):
        bt(i+str(j))
for x in range(10):
    bt(str(x))
dap.sort()
try:
    print(dap[n-1])
except:
    print(-1)