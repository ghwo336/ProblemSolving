di={
    'J':'O',
    'O':'I',
    'I':'J'
}

n=int(input())
s=input()
for x in s:
    print(di[x],end='')