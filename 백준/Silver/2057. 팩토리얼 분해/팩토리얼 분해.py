li=[1,1]
n=int(input())
if n==0:
    print('NO')
else:
    for x  in range(2,28):
        li.append(li[-1]*x)
    for y in range(28):
        if n>=li[27-y]:
            n-=li[27-y]
    if n:
        print('NO')
    else:
        print('YES')
    
    