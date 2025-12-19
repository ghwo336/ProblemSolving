import sys
dap=0
for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    a,b=line.split('.')
    dap+=(int(a)*100+int(b))
print(f"{dap//100}.{dap%100:02d}")