n=int(input())
graph=[[] for _ in range(n)]

for x in range(n):
    s=input()
    for y in range(len(s)):
        if s[y]=="Y":
            graph[x].append(y)

st=[0 for _ in range(n)]

for x in range(n):
    s=set()
    s.add(x)
    for y in graph[x]:
        s.add(y)
        for z in graph[y]:
            s.add(z)
    st[x]=len(s)
print(max(st)-1)