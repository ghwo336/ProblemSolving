N=int(input())
s=input()
if N<3:
    print("No")
else:
    pandan=0
    for x in range(N-2):
        if s[x]=='o' and s[x+1]=='o' and s[x+2]=='o':
            pandan=1
    if pandan:
        print("Yes")
    else:
        print("No")