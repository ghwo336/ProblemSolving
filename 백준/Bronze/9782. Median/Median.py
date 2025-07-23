a=0
while (True):
    a+=1
    li=list(map(int,input().split()))
    if li[0]==0:
        break
    n=li[0]
    li=li[1:]
    
    if n%2==0:
        print(f'Case {a}: {(li[n//2-1]+li[n//2])/2:.1f}')
    else:
        print(f'Case {a}: {li[n//2]:.1f}')