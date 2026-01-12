import re
s = input()
li = re.findall(r'[^.?]+[.?]?', s)
for x in range(len(li)):
    if '?' in li[x]:
        li2=list(li[x].split())
        fiv=0
        print('Forty-two',end=' ')
        for y in li2:
            if fiv:
                if '?' in y:
                    print(y[:len(y)-1],end='. ')
                else:
                    print(y,end=' ')
            if y=='What':
                fiv=1
        if x!=len(li)-1:
            print('')