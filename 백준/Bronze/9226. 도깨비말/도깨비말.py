s={'a','e','i','o','u'}
while True:
    a=input()
    sl=len(a)
    if a=='#':
        break
    li=list(a)
    for x in range(sl):
        if li[x] not in s:
            li.append(li[x])
        else:
            break
    dap=''
    added=len(li)-sl
    for x in range(added,len(li)):
        dap+=li[x]
    print(dap+'ay')
        
        
    
    
        
    