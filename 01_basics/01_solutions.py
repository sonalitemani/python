age = input('enter your age : ')
age = int(age)
if age < 13:
    print('chield')
elif age < 20:
    print('teenager')
elif age <60:
    print('Adult')
else:
    print('senior')