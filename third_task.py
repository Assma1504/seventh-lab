myTupleDays = ("Monday","Tuesday","Wednesday","Thursday","Friday", "Saturday","Sunday")
numberOfDays = int(input("How many free days you want: "))
freeDaysCount =list(myTupleDays[-numberOfDays:])
workingDaysCount =list(myTupleDays[:-numberOfDays])
# print (myTupleDays[-numberOfDays:])
# print (myTupleDays[:-numberOfDays])

print (f"Your free days are: {freeDaysCount}")
print (f"You will work on: {workingDaysCount}")