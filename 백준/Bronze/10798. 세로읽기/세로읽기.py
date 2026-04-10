li=[]
f=0
for x in range(5):
    a=input()
    li.append(a)
    f=max(f,len(a))
for x in range(f):
    for y in range(5):
        try:
            print(li[y][x],end='')
        except:
            continue

    