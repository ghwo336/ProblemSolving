N=int(input())
di={"STRAWBERRY":0,"BANANA":0,"LIME":0,"PLUM":0}
for x in range(N):
    a,b=input().split()
    di[a]+=int(b)
pandan=True
for x in di:
    if di[x]==5:
        print("YES")
        pandan=False
        break

if pandan:
    print("NO")