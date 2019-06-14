sb,cr=map(int,input().split())
a=[]
for x in input().split():
  a.append(int(x))
d=a.count(cr)
if(d>0):
  print("yes")
else:
  print("no")
