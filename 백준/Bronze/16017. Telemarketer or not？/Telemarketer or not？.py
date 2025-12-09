li=[]
for x in range(4):
    a=int(input())
    li.append(a)
s={8,9}
if li[0] in s and li[-1] in s and li[1]==li[2]:
    print('ignore')
else:
    print('answer')