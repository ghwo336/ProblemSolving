di={'Poblano':1500,
   'Mirasol':6000,
    'Serrano':15500,
    'Cayenne':40000,
    'Thai':75000,
    'Habanero':125000
   }


t=int(input())
dap=0
for x in range(t):
    a=input()
    dap+=di[a]
print(dap)