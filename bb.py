s=input()
b=0
a=0
for w in s:
    if(w.isalpha()==True):
        a=a+1
    elif(w.isdigit()==True):
        b=b+1
if(a>0 and b>0):
    print("Yes")
else:
    print("No")
