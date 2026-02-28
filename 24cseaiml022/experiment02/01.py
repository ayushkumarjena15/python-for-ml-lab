p=float(input("enter the principle amount"))
r=float(input("enter the rate of intrest"))
t=int(input("enter the years"))
n=int(input('enter the times the intrest compounding for a year'))
i=(p*t*r)/100
a=p*((1+( r/n))**(n*t))
print("The simple intrest is ",i,"\nThe compound intrest is ",a)