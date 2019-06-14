in1 = int(input())
if in1 > 1:
   for i in range(2,in1):
       if (in1 % i) == 0:
           print("no")
           break
   else:
       print("yes")
else:
   print("no")
