n=int(input())
n=n%8
if n ==1 : 
    print(1)
elif n==0 or n==2 : 
    print(2)
elif n==3 or n==7 : 
    print(3)
elif n==4 or n==6: 
    print(4)
else: 
    print(5)