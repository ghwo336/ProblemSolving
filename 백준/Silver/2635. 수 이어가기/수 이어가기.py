n=int(input())
dapli=[]
dap=0
for x in range(1,n+1):
    li=[n,x]
    while True:
        if li[-2]-li[-1]>=0:
            li.append(li[-2]-li[-1])
        else:
            if dap<len(li):
                dap=len(li)
                dapli.append(li)
            break
print(dap)
print(*dapli[-1])
                
        
    