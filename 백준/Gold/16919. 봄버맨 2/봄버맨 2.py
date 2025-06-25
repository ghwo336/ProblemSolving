graph=[]
r,c,n=map(int,input().split())
for x in range(r):
    li=list(input())
    graph.append(li)

bombs=[]
for x in range(r):
    for y in range(c):
        if graph[x][y]=='O':
            bombs.append((x,y))
if n%2==0:
    for x in range(r):
        print("O"*c)
else:
    if n==1:
        for x in range(r):
            a=''
            for y in range(c):
                a+=graph[x][y]
            print(a)
    else:
        for bomb in bombs:
            if bomb[0]-1>=0:
                graph[bomb[0]-1][bomb[1]]='O'
            if bomb[0]+1<r:
                graph[bomb[0]+1][bomb[1]]='O'
            if bomb[1]-1>=0:
                graph[bomb[0]][bomb[1]-1]='O'
            if bomb[1]+1<c:
                graph[bomb[0]][bomb[1]+1]='O'
            
        for x in range(r):
            for y in range(c):
                if graph[x][y]=='O':
                    graph[x][y]='.'
                else:
                    graph[x][y]='O'
        if n%4==3:
            for x in range(r):
                a=''
                for y in range(c):
                    a+=graph[x][y]
                print(a)
        else:
            bombs2=[]
            for x in range(r):
                for y in range(c):
                    if graph[x][y]== 'O':
                        bombs2.append((x,y))
            for bomb in bombs2:
                if bomb[0]-1>=0:
                    graph[bomb[0]-1][bomb[1]]='O'
                if bomb[0]+1<r:
                    graph[bomb[0]+1][bomb[1]]='O'
                if bomb[1]-1>=0:
                    graph[bomb[0]][bomb[1]-1]='O'
                if bomb[1]+1<c:
                    graph[bomb[0]][bomb[1]+1]='O'
            for x in range(r):
                a=''
                for y in range(c):
                    if graph[x][y]=='O':
                        a+='.'
                    else:
                        a+='O'
                print(a)
            