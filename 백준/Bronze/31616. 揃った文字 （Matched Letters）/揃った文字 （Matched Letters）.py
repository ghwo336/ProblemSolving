a=int(input())
b=input()
s=set()

for x in b:
    s.add(x)

if len(s)==1:
    print("Yes")
else:
    print("No")