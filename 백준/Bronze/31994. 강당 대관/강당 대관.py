di=dict( )
for x in range(7):
    a,b=input().split()
    di[int(b)]=a

print(di[max(di)])