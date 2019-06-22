sb1,sb2=input().split()  
sb1=int(sb1)  
sb2=int(sb2)   
v=list(map(int,input().split()))
count=0  
for i in range(len(v)):
  for j in range(i+1,len(v)):
    if (v[i]+v[j]==sb2):
      count+=1
      break
if(count):
  print("yes")
else:
  print("no")
