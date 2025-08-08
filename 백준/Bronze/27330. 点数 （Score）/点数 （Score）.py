n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
score=0
for x in a:
    score+=x
    for y in b:
        if score==y:
            score=0
print(score)