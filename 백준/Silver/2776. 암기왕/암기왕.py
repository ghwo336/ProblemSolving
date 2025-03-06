def sol():
    n=int(input())
    li=list(map(int,input().split()))
    li.sort()
    m=int(input())
    li2=list(map(int,input().split()))
    for x in li2:
        start=0
        pandan=0
        end=n-1
        while start<=end:
            mid=(start+end)//2
            if li[mid]>x:
                end=mid-1
            if li[mid]<x:
                start=mid+1
            if li[mid]==x:
                pandan=1
                break
        if pandan:
            print(1)
        else:
            print(0)
    
    




t=int(input())
for x in range(t):
    sol()