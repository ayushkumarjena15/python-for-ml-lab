n=int(input("Entrer a number"))
s=str(n)
if(s==s[::-1]):
    print("number is Palindrome")
else:
    print("Number is not Palindrome")