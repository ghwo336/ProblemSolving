n=int(input())
t=input()
talchul=[]
dap=0
for _ in range(n):
    hubo=input()
    l=len(hubo)
    for kan in range(1,l):
        try:
            for start in range(l):
                now=start
                fiv=''
                fiv+=hubo[now]
                while True:
                    try:
                        fiv+=hubo[now+kan]
                        if len(fiv)==len(t):
                            break
                        now+=kan
                    except:
                        break
                if fiv == t:
                    dap+=1
                    a=talchul[dap]
        except:
            break
            
                    
                
print(dap)
