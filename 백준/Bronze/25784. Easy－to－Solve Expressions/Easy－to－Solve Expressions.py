li=list(map(int,input().split()))
li.sort()
if li[0]+li[1]==li[2]:
    print(1)
elif li[0]*li[1]==li[2]:
    print(2)
else:
    print(3)