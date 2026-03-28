a=input()
di={
    'A':0,
    'B':0
}
for x in range(len(a)):
    if x%2==1:
        di[a[x-1]]+=int(a[x])
if di['A']>di['B']:
    print('A')
else:
    print('B')