age = input('Enter your age : ')
age = int(age)
price = 0
discount = 0
day = input('Enter a day : ')

price = 12 if age >= 18 else 8

if day == 'wednesday' or day == 'Wednesday':
    discount = 2

total_price = price - discount
message = "Movie ticket price is {} "

print(message.format(total_price))
    