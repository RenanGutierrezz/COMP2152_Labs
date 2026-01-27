mondayClass = {"Alice","Bob","Andrea","Renan"}
wednesdayClass = {"Bob", "Natalia", "Gustavo", "joao"}

mondayClass.add("Grace")
print(f"Monday Class: {mondayClass}")
print(f"Wednesday Class: {wednesdayClass}")
bothClasses = mondayClass & wednesdayClass
print(f"Attended both class: {bothClasses}")
allStudents = mondayClass | wednesdayClass
print(f"Attended either class: {allStudents}")
# using difference (-)
onlyMonday =  mondayClass - wednesdayClass
print("Only Monday: ", onlyMonday)
onlyOne = mondayClass ^ wednesdayClass
print(f"Only one class: {onlyOne}")
print(f"Is monday subset of all students? {mondayClass <= allStudents}")
