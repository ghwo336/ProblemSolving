n=input()
l=len(n)
if l%10!=0:
    l+=1
for x in range(l):
    print(n[10*x:min(10*(x+1),len(n))])
    