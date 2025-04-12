while True:
    try:
        a=input()
        dap=''
        for x in a:
            if x=='I':
                dap+='E'
            elif x=='E':
                dap+='I'
            elif x=='e':
                dap+='i'
            elif x=='i':
                dap+='e'
            else:
                dap+=x
        print(dap)
    except EOFError:
        break