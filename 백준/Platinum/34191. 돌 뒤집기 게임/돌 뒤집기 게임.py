n=int(input())
s=input()
three=0
four=0
now=0
Hnum=0
for x in range(n):
    if s[x]=='H':
        Hnum+=1
        now+=1
        if now==4:
            three-=1
            four+=1
        elif now>=3:
            three+=1
    else:
        now=0

if three:
    print('First')
elif four and (Hnum-four)%2==1:
    print('First')
elif four==0 and Hnum%2==1:
    print('First')
else:
    print('Second')
    