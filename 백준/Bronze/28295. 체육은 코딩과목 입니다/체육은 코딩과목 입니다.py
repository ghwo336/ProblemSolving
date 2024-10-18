li=['N','E','S','W']
h=0
for x in range(10):
    h+=int(input())
print(li[h%4])