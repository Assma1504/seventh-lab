#=================================== Option 1 ============================================================


# import random
# myRange = range(1,10)
# myList = []
repeatedItem = []

# for item in myRange:
#     myList.append(random.randint(1,15))

# for item in myList:
#     if myList.count(item) > 1 :
#         repeatedItem.append(item)

# print(f"Here is the repeated items in our list: {repeatedItem}")

#=================================== Option 2 ============================================================

listItems=[1,1,2,3,4,5,6,7,7,7,7,7,8,8,8,9,9,9]
for item in listItems:
    if listItems.count(item)> 1:
        repeatedItem.append(item)
# Here if we want to print just one value, I think we need recursive function
print(f"Here is the repeated items in our list: {repeatedItem}") 
