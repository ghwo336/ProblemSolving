n=int(input())
l=input()
now=0
s=0
b=0
while True:
    try:
        if l[now]=='s':
            s+=1
            now+=8
        elif l[now]=='b':
            b+=1
            now+=7
    except:
        break
if b>s:
    print("bigdata?")
elif b<s:
    print("security!")
else:
    print("bigdata? security!")
        