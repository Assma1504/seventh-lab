def check_number():

    myList = [15,22,36,52,99]
    userInput =int(input("Please inter a number: "))
    if userInput in myList:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")

check_number()