
studentMyGroup = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов", "Попов", "Васильев", "Новиков", "Фёдоров", "Морозов"]
studentOtherGroup = ["Алексеев", "Белов", "Дмитриев", "Егоров", "Жуков", "Зайцев", "Киселёв", "Лебедев", "Макаров", "Никитин"]

#=================================== Option 1 ============================================================
# studentsList =[]
# myRange = range(0,10)

# for item in myRange:
#     if item %2 == 0:
#         studentsList.append(studentMyGroup[item])
#     else:
#         studentsList.append(studentOtherGroup[item])

# tupleStudents = tuple(studentsList)
# print(studentMyGroup)
# print(studentOtherGroup)
# print(tupleStudents)
# print(len(tupleStudents))
# studentsList.sort()
# sortedStudentsTuple = tuple(studentsList)
# print(sortedStudentsTuple)
# print (tupleStudents.count("Иванов")) if "Иванов" in tupleStudents else print("No")


#=================================== Option 2 ============================================================
tupleStudents = tuple(studentMyGroup[0:5] + studentOtherGroup[0:5])
sortedStudentsTuple = tuple(sorted(tupleStudents))
print(studentMyGroup)
print(studentOtherGroup)
print(tupleStudents)
print(len(tupleStudents))
print(sortedStudentsTuple)
print (tupleStudents.count("Иванов")) if "Иванов" in tupleStudents else print("No")