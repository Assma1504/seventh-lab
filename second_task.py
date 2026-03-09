# import random

# myRange = range(1,10)
# myList = []
repeatedItem = []

# for item in myRange:
#     myList.append(random.randint(1,15))

# for item in myList:
#     if myList.count(item) > 1 :
#         repeatedItem.append(item)
        # print(myList.count(item))

# print(myList)
# print(countReapted)
# print(repeatedItem)

listItems=[1,1,2,3,4,5,6,7,7,7,7,7,8,8,8,9,9,9]
for item in listItems:
    if listItems.count(item)> 1:
        repeatedItem.append(item)

print(repeatedItem) 
