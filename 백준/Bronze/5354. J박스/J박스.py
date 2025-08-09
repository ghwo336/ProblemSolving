def sol():
    n=int(input())
    if n==1:
        print('#')
    elif  n==2:
        print('##')
        print('##')
    else:
        print('#'*n)
        for x in range(n-2):
            print('#'+'J'*(n-2)+'#')
        print('#'*n)
    print('')


a=int(input())
for x in range(a):
    sol()