n,m=map(int,input().split())
s=list(input())
for x in range(n):
    now=int(s[x])
    p=10-now
    if p<=m and now!=0:
        m-=p
        s[x]='0'
m=m%10
s[-1]=str((int(s[-1])+m)%10)
for i in s:
    print(i,end='')
        
    
    