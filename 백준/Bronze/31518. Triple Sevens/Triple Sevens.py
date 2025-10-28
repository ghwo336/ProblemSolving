n=int(input())
fiv=1
for x in range(3):
    li=list(map(int,input().split()))
    if 7 not in  li:
        fiv=0
if fiv:
    print('777')
else:
    print(0)