ns=0
we=0
n=int(input())
a=input()
for x in a:
    if x=='N':
        ns+=1
    elif x=='S':
        ns-=1
    elif x=='W':
        we+=1
    else:
        we-=1
print(abs(ns)+abs(we))