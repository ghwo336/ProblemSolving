n=int(input())
for _ in range(n):
    p1=0
    p2=0
    m=int(input())
    for x in range(m):
        a,b=input().split()
        if a!=b:
            if a=='R' and b=='S':
                p1+=1
            elif a=='S' and b=='P':
                p1+=1
            elif a=='P' and b=='R':
                p1+=1
            else:
                p2+=1
    if p1>p2:
        print('Player 1')
    elif p1==p2:
        print('TIE')
    else:
        print('Player 2')
            