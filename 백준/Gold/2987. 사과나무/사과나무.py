li=[]
for x in range(3):
    a,b=map(int,input().split())
    li.append([a,b])
dap=0
dap+=li[0][0]*(li[1][1]-li[2][1])
dap+=li[1][0]*(li[2][1]-li[0][1])
dap+=li[2][0]*(li[0][1]-li[1][1])
print(abs(dap)/2)
pandan=abs(dap)
n=int(input())
dap2=0
for x in range(n):
    p,q=map(int,input().split())
    pandan2=0
    hubo=0
    #p,q를 li[0]대신 넣었을때
    hubo+=p*(li[1][1]-li[2][1])
    hubo+=li[1][0]*(li[2][1]-q)
    hubo+=li[2][0]*(q-li[1][1])
    pandan2+=(abs(hubo))

    #p,q를 li[1]대신 넣었을때
    hubo=0
    hubo+=li[0][0]*(q-li[2][1])
    hubo+=p*(li[2][1]-li[0][1])
    hubo+=li[2][0]*(li[0][1]-q)
    pandan2+=(abs(hubo))   
    
    #p,q를 li[2]대신 넣었을때
    hubo=0
    hubo+=li[0][0]*(li[1][1]-q)
    hubo+=li[1][0]*(q-li[0][1])
    hubo+=p*(li[0][1]-li[1][1])
    pandan2+=(abs(hubo))
    if int(pandan2)==int(pandan):
        dap2+=1;
    

print(dap2)
    
        