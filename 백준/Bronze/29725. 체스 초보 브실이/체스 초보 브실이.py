di = {
    'K': 0, 'k': 0,   
    'P': 1, 'p': -1,   
    'N': 3, 'n': -3,   
    'B': 3, 'b': -3,   
    'R': 5, 'r': -5,   
    'Q': 9, 'q': -9    
}
dap=0
for x in range(8):
    a=input()
    for y in a:
        if y in di:
            dap+=di[y]
print(dap)
            