s=input()
n=0
for j in range(len(s)):
    if(s[j].isdigit()!=True and s[j].isalpha()!=True):
        n=n+1
print(n)
