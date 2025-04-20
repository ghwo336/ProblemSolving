li=[0,0,0,0]
a=input()
for x in a:
    if x=="U":
        li[0]+=1
    if x=="A":
        li[1]+=1
    if x=="P":
        li[2]+=1
    if x=="C":
        li[3]+=1
k=''
if li[0]==0:
    k+='U'
if li[1]==0:
    k+='A'
if li[2]==0:
    k+='P'
if li[3]==0:
    k+='C'
print(k)