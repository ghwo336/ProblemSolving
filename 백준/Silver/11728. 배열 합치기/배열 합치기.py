a,b=map(int,input().split())
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
li3=li1+li2
li3.sort()
print(*li3)