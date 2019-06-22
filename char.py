xa=int(input())
yb=list(map(int,input().split()))
n=s=[]
for i in range(0,xa):
    n=list(bin(yb[i]))
    n=n[2:]
    s.append(n)
s=sorted(s)
s=s[::-1]
for i in range(0,xa):
    p=1
    z=0
    for j in range(len(s[i])-1,-1,-1):
        z=z+(int(s[i][j])*p)
        p=p*2
    print(z)
