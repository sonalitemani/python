marks = input('Enter your marks : ')
marks = int(marks)

if marks > 100:
    print('marks cannot be greater then 100')
    exit()
if marks >= 90:
    grade = 'A'
elif marks >=80:
    grade = 'B'
elif marks >=70:
    grade ='C'
elif marks >=70:
    grade ='D'
else:
    grade= 'F'
message = "your marks is {} so your grade is {}"
print(message.format(marks,grade))