n,k,t=map(int,input().split())
li=list(map(int,input().split()))
start=0
end=n-1
li.sort()
li.reverse()
while start<end:
    if t<=0:
        break
    if li[start]+li[end]<k:
        if t>=li[end]:
            li[start]+=li[end]
            t-=li[end]
            li[end]=0
            end-=1
        else:
            break
    elif li[start]+li[end]==k:
        if t>=li[end]:
            li[start]+=li[end]
            t-=li[end]
            li[end]=0
            start+=1
            end-=1
        else:
            break
    else:
        if t>=k-li[start]:
            li[end]-=(k-li[start])
            t-=(k-li[start])
            li[start]=k
            start+=1
        else:
            break

dap=1
for x in li:
    if x and x<k:
        dap=0
if dap:
    print('YES')
else:
    print('NO')

