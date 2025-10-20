n,m=map(int,input().split())
li=[0 for _ in range(101)]
now=0
for x in range(n):
    time,speed=map(int,input().split())
    for y in range(now+1,now+time+1):
        li[y]=-speed
    now+=time
now=0
for x in range(m):
    time,speed=map(int,input().split())
    for y in range(now+1,now+time+1):
        li[y]+=speed
    now+=time    
print(max(max(li),0))
    