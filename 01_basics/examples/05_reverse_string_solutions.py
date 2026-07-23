name = 'ReverseThisString'
reversed_name =''
for i in range(len(name) -1 ,0,-1):
    reversed_name = reversed_name + name[i]
print(reversed_name)