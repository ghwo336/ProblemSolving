n=int(input())
a=''
for x in range(n):
    li=list(input().split())
    a=li
print(len(li)-1)
for x in range(1,len(li)):
    print(li[x])
    