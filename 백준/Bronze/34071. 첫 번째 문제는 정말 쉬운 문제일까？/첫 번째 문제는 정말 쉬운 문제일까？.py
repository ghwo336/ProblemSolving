n=int(input())
li=[]
for x in range(n):
    a=int(input())
    li.append(a)
f=li[0]
li.sort()
if f==li[0]:
    print("ez")
elif f==li[-1]:
    print("hard")
else:
    print("?")