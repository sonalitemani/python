while True:
    number = input('Enter a number')
    int_num = int(number)
    if 0 < int_num <= 10:
        print("Your number is between 1 to 10")
        break
    else:
        print('Invaild input try again')
    
    