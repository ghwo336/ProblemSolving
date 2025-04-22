a,b=map(int,input().split())
li=[]
for x in range(a):
    li.append(int(input()))
k=b//sum(li)
for x in li:
    print(x*k)