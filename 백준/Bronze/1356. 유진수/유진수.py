a=input()
l=len(a)
pandan=0
for x in range(1,l):
    p=a[:x]
    q=a[x:]
    i=1
    j=1
    for y in p:
        i*=int(y)
    for y in q:
        j*=int(y)
    if i==j:
        pandan=1
if pandan:
    print("YES")
else:
    print("NO")
    