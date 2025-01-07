p=0
while True:
    p+=1
    n=int(input())
    if n==0:
        break
    if (n%2==1):
        print(f"{p}. odd {n//2}")
    else:
        print(f"{p}. even {n//2}")