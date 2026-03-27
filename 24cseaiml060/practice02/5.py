d={}

for i in range(3):
    k=input("enter the key: ")
    v=input("Enter the value: ")
    d[k]=v

for k,v in d.items():
    print(k,":",v)
print()

for i in d.values():
    print(i)