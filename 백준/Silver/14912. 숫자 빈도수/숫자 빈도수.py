n,d=map(int,input().split())
li=[0]*10
for x in range(1,n+1):
    for y in str(x):
        li[int(y)]+=1
print(li[d])