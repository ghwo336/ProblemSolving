n=int(input())
li=[]
for x in range(n):
    a,b=input().split()
    li.append([b,a])
li.sort()
print(li[-1][1])