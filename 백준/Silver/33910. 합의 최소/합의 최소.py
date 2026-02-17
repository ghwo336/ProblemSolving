n=int(input())
li=list(map(int,input().split()))
li.reverse()
for x in range(1,n):
    li[x]=min(li[x],li[x-1])
print(sum(li))