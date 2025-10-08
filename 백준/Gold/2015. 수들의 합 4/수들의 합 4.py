import sys
input=sys.stdin.readline
n,k=map(int,input().split())
li=list(map(int,input().split()))
sumdi={0:1}
hap=[li[0]]
dap=0
for x in range(1,n):
    hap.append(hap[-1]+li[x])
for x in hap:
    if x-k in sumdi:
        dap+=sumdi[x-k]
    if x not in sumdi:
        sumdi[x]=1
    else:
        sumdi[x]+=1
print(dap)