n=int(input())
li=[]
for x in range(n):
    a=int(input())
    li.append(a)
li.sort()
li2=[]
for x in range(len(li)//2):
    li2.append(li[x]+li[-x-1])
print(min(li2))