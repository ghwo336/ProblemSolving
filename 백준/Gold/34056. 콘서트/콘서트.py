import sys
input=sys.stdin.readline

n=int(input())
w=list(map(int,input().split()))
t=int(input())
for _ in range(t):
    li=list(map(int,input().split()))
    if li[0]==1:
        sound=li[2]
        for x in range(li[1],n):
            if sound>0:
                if w[x]<sound:
                    sound-=w[x]
                    w[x]*=2
                else:
                    w[x]+=sound
                    break
            else:
                break
        sound=li[2]
        for y in range(li[1]):
            now=li[1]-y-1
            if sound>0:
                if w[now]<sound:
                    sound-=w[now]
                    w[now]*=2
                else:
                    w[now]+=sound
                    break
            else:
                break

    else:
        print(w[li[1]-1])
            
    
