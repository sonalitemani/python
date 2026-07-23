fruitList = {
    "apple" : {"green":"unripe","yellow":"ripe","red":"very ripe"},
    "banana" : {"green":"unripe","yellow":"ripe","brown":"very ripe"},
    "cherry" : {"red":"ripe","black":"very ripe"},
    "orange" : {"orange":"ripe"},
    "grape" : {"green":"unripe","purple":"ripe"}
}
fruit = input('Enter the fruit name: ')
color = input('Enter the color: ')
if fruit in fruitList and color in fruitList[fruit]:
    print(f"The {fruit} is {color} then it is {fruitList[fruit][color]}")
else:
    print("Invalid input")