import sys
input=sys.stdin.readline


def find(n):
    if parents[n]!=n:
        parents[n]=find(parents[n])
    return parents[n]
def union(node1,node2):
    r1=find(node1)
    r2=find(node2)
    parents[max(r1,r2)]=min(r1,r2)
    


dap=0

visit=set()
di=dict()
V,E=map(int,input().split())
cha=[0 for _  in range(V+1)]
parents=[x for x in range(V+1)]
for x in range(E):
    chul,do=map(int,input().split())
    cha[chul]+=1
    cha[do]+=1
    visit.add(chul)
    visit.add(do)
    union(chul,do)

evenparents=set()
for x in range(V+1):
    if x in visit:
        if find(x) not in di:
            di[find(x)]=[]

for x in range(V+1):
    if x in visit:
        di[find(x)].append(x)

for x in di:
    fiv=0
    for y in di[x]:
        if cha[y]%2==1:
            fiv+=1
    dap+=max(0,(fiv-2)//2)
print(dap+len(di)-1+V-len(visit))
        