N=int(input())
li=[0,0,0]
li2=[0,0,0]
for x in range(N):
    a,b,c=map(int,input().split())
    d,e,f=a,b,c
    a+=max(li[0],li[1])
    b+=max(li)
    c+=max(li[1],li[2])
    d+=min(li2[0],li2[1])
    e+=min(li2)
    f+=min(li2[1],li2[2])
    li[0]=a
    li[1]=b
    li[2]=c
    li2[0]=d
    li2[1]=e
    li2[2]=f

print(max(li),min(li2))
    