n=int(input())
a=input()
f=0
for x in a:
    if x=='O':
        f+=1
if 2*f>=n:
    print('Yes')
else:
    print('No')