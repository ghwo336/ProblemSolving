che=[True for _ in range(2000)]
che[0],che[1]=False,False
for x in range(2000):
    if che[x]:
        for y in range(x*2,2000,x):
            che[y]=False

def sol(n):
    for i in range(2000):
        if che[i]:
            for j in range(i+1,2000):
                if che[j]:
                    if i*j>n:
                        print(i*j)
                        return
                    else:
                        break
n=int(input())
sol(n)