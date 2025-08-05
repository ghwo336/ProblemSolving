n=int(input())
for x in range(1,n+1):
    li=list(input().split())
    li.reverse()
    print(f'Case #{x}:',end=' ')
    for y in li:
        print(y,end=' ')
    print('')