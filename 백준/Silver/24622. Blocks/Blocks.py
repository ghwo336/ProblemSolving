n=int(input())
li=[]
li2=[]
for x in range(4):
    a=input()
    li.append(a)
for x in range(4):
    for y in range(4):
        if x!=y:
            for z in range(4):
                if x!=z and y!=z: 
                    for w in range(4):
                        if x!=w and y!=w and z!=w:
                            first=li[x]
                            second=li[y]
                            third=li[z]
                            fourth=li[w]
                            for i in range(6):
                                for j in range(6):
                                    for k in range(6):
                                        for p in range(6):
                                            q=first[i]+second[j]+third[k]+fourth[p]
                                            li2.append(q)


for x in range(n):
    a=input()
    l=len(a)
    pandan=0
    for y in li2:
        p=1
        for z in range(l):
            if a[z]!=y[z]:
                p=0
                break
        if p:
            pandan=1
            break
    if pandan:
        print("YES")
    else:
        print("NO")
            
            
                            