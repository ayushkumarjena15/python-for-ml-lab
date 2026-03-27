d={
    'Name':'Ram',
    'Roll':22,
    'Mark':27.4
}
print(sorted(d.items(),key=str))
print(sorted(d.items(),key=lambda x:x[1]))

