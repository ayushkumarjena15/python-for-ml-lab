n=int(input("Enter a 5 digit number"))
s=str(n)
for i in range(1,6):
    if(i%2!=0):
        print(s[i-1])