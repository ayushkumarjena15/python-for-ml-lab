s=input("Enter the string")
print("It's reverse is: ",s[::-1])

v_count=0
c_count=0
for i in s:
    if i in "AEIOUaeiou":
        v_count+=1
    else:
        c_count+=1
print("Number os vowels in it is: ",v_count,"\nNumber of consonant is: ",c_count)