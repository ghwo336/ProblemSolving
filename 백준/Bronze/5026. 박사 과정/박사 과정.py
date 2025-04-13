t=int(input())
for x in  range(t):
    k=input()
    if k=='P=NP':
        print("skipped")
    else:
        a,b=k.split("+")
        print(int(a)+int(b))