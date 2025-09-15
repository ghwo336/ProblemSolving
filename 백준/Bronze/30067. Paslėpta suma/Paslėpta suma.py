li=[]
for x in range(10):
    li.append(int(input()))
s=sum(li)
for x in li:
    if x*2==s:
        print(x)
        break