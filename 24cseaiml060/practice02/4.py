d={
    'name':'Ram',
    'Roll':22,
    'Mark':27.4
}

print(d.items())
print(type(d.items()))


'''
print(d)
print(type(d))
print(d.values())
print(d.keys())
'''


for i in d:
    print(i)
    v=input("Enter value: ")
    d[i]=v
print()
for i in d.items():
    print(i[0])
    print(i[1])