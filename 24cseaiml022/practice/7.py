s=input("Enter the string: ")
s2=''.join(reversed(s))
if(s==s2):
    print("Palindrome")
else:
    print("Not palindrome")