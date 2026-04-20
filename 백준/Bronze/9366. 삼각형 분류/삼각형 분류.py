t=int(input())
for x in range(t):
    print(f'Case #{x+1}: ',end='')
    li=list(map(int,input().split()))
    li.sort()
    if li[0]+li[1]<=li[2]:
        print('invalid!')
        continue
    if len(set(li))==1:
        print('equilateral')
    elif len(set(li))==2:
        print('isosceles')
    else:
        print('scalene')