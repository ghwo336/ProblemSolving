n=int(input())
li=[0,0,0,0,0]
a=input()
for x in range(n):
    if a[x]=='H':
        li[0]+=1
    elif a[x]=='I':
        li[1]+=1
    elif a[x]=='A':
        li[2]+=1
    elif a[x]=='R':
        li[3]+=1
    elif a[x]=='C':
        li[4]+=1
print(min(li))