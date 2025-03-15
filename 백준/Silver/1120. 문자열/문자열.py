a,b=input().split()
la=len(a)
lb=len(b)
dap=la
for start in range(lb-la+1):
    d=0
    for x in range(start,start+la):
        if a[x-start]!=b[x]:
            d+=1
    dap=min(dap,d)
print(dap)