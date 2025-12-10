li=[]
for x in range(4):
    a=int(input())
    li.append(a)

if li[0]<li[1]<li[2]<li[3]:
    print('Fish Rising')
elif li[0]>li[1]>li[2]>li[3]:
    print('Fish Diving')
elif li[0]==li[1] and li[1] == li[2] and li[2] == li[3]:
    print('Fish At Constant Depth')
else:
    print('No Fish')
