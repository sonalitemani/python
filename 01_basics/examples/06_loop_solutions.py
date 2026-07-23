input_str = 'teeter'
print_char = ''
for i in range(len(input_str)):
    if(input_str.count(input_str[i]) == 1):
        print_char = input_str[i]
        break
else:
    print('no unique char')

print(print_char)
    