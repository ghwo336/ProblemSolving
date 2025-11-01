def bt(number,hap,lis,di):
    if number == len(lis):
        di[hap]=di.get(hap,0)+1
        return
    bt(number+1,hap,lis,di)
    bt(number+1,hap+lis[number],lis,di)
        
    
n,m=map(int,input().split())
li=list(map(int,input().split()))
left=li[:n//2]
right=li[n//2:]
leftdi=dict()
rightdi=dict()
bt(0,0,left,leftdi)
bt(0,0,right,rightdi)
dap=0
for x in range(-3000000,3000001):
    if x in leftdi and m-x in rightdi:
        dap+=(leftdi[x]*rightdi[m-x])

if m==0:
    dap-=1
print(dap)        
