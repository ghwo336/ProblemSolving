mod=900528
s=input()
f=list(input())
f.reverse()
di=dict()
for x in range(1,len(s)+1):
    di[s[x-1]]=x
dap=0
w=1
for x in range(len(f)):
    dap+=(di[f[x]]*w)
    w*=len(s)
    dap%=mod
    w%=mod
print(dap)