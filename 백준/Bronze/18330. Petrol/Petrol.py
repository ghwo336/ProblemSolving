a=int(input())
b=int(input())
b+=60
if b>=a:
    print(a*1500)
else:
    print(b*1500+(a-b)*3000)