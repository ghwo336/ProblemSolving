a=int(input())
li=list(map(int,input().split()))
s=sum(li)
if s%3==0:
    print('yes')
else:
    print('no')