s1,s2=input().split()  
s1=int(s1)  
s2=int(s2)   
v=list(map(int,input().split()))
count=0  
for i in range(len(v)):
  for j in range(i+1,len(v)):
    if (v[i]+v[j]==s2):
      count+=1
      break
if(count):
  print("yes")
else:
  print("no")
