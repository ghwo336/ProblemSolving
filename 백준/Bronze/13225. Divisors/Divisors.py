li=[0 for _ in range(10001)]
for x in range(1,10001):
    for y in range(1,x+1):
        if x%y==0:
            li[x]+=1
n=int(input())
for x in range(n):
    a=int(input())
    print(a,li[a])