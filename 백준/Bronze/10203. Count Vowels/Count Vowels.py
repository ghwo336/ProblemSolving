n=int(input())
for x in range(n):
    a=input()
    dap=0
    for y in a:
        if y in 'aeiou':
                dap+=1
    print(f'The number of vowels in {a} is {dap}.')
    