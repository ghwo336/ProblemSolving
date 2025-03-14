a=input()
s=input()
l1=len(a)
l2=len(s)
now=0
dap=0
if l1<l2:
    print(0)
else:
    while(now+l2<=l1):
        pandan=1
        for x in range(l2):
            if a[now+x]!=s[x]:
                pandan=0
                break
        if pandan:
            dap+=1
            now+=l2
        else:
            now+=1
    print(dap)
    