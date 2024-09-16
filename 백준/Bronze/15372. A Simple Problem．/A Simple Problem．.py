import sys
input=sys.stdin.readline
li=[]
for x in range(200001):
    li.append(x**2)
T=int(input())
for _ in range(T):
    a=int(input())
    print(li[a])