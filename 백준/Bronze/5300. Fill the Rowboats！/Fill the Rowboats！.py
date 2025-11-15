n=int(input())
for x in range(1,n+1):
    print(x,end=' ')
    if x%6==0 or x==n:
        print('Go!',end=' ')
        
    