li=[]
l=0
n=int(input())
for x in range(n):
    li2=list(input().split())
    a=li2[0]
    b=li2[-1]
    if a=="push":
        li.append(b)
        l+=1
    elif a=="pop":
        if l==0:
            print(-1)
        else:
            l-=1
            print(li.pop())
    elif a=="size":
        print(l)
    elif a=="empty":
        if l==0:
            print(1)
        else:
            print(0)
    elif a=="top":
        if li:
            print(li[-1])
        else:
            print(-1)
    
            