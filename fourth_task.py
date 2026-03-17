studentMyGroup = ["Иванов","Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов", "Попов", "Васильев", "Новиков", "Фёдоров", "Морозов"]
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
# print(f"Students from our group: {studentMyGroup}")
# print(f"Students from the other group: {studentOtherGroup}")
# print(f"Students from bouth groups: {tupleStudents}")
# print(f"The number of students: {len(tupleStudents)}")
# studentsList.sort()
# sortedStudentsTuple = tuple(studentsList)
# print(f"Here is the sorted tuple: {sortedStudentsTuple}")
# print ("There is Иванов") if "Иванов" in tupleStudents else print("No")
# print (tupleStudents.count("Иванов"))

#=================================== Option 2 ============================================================
tupleStudents = tuple(studentMyGroup[0:5] + studentOtherGroup[0:5])
sortedStudentsTuple = tuple(sorted(tupleStudents))
print(f"Students from our group: {studentMyGroup}")
print(f"Students from the other group: {studentOtherGroup}")
print(f"Students from bouth groups: {tupleStudents}")
print(f"The number of students: {len(tupleStudents)}")
print(f"Here is the sorted tuple: {sortedStudentsTuple}")
print ("There is Иванов") if "Иванов" in tupleStudents else print("No")
print (tupleStudents.count("Иванов"))