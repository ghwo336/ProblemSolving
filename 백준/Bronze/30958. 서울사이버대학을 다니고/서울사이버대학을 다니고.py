li=[0 for _ in range(26)]
n=int(input())
b=input()
for x in b:
    if x!=' ' and x!=','  and x!='.':
        li[ord(x)-97]+=1
print(max(li))