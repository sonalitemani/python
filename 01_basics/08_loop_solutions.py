items = ['apple','banana','cherry','banana','orange','apple','mango']

# for i  in items:
#     if items.count(i) > 1:
#         print(i)
#         break
# else:
#     print('no unique items')

unique_item = set()
    
for item in items:
    if item in unique_item:
        print('Dulicate item',item)
        break
    unique_item.add(item)
else:
    print('no unique items')