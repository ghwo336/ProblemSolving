while True:
    a=input()
    if a=="***":
        break
    else:
        a=list(a)
        a.reverse()
        for x in a:
            print(x,end='')
        print('')