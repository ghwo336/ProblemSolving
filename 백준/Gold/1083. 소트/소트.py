n=int(input())
li=list(map(int,input().split()))
s=int(input())
index=0
while s>0 and index<n:
    fiv=li.index((max(li[index:index+s+1])))
    if fiv != index:
        li[fiv],li[fiv-1]=li[fiv-1],li[fiv]
        s-=1
    else:
        index+=1
print(*li)