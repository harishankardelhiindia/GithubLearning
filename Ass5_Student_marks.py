student_details = {"John":85.6, "Alice": 90.7, "Raja": 98.0,"James": 100.0}
print("Below are the available student names")
for student in student_details:
    print(student)
student_name = input("Enter the Student's name: ")
i = 1
for student in student_details:
    if student == student_name:
        print(student_details[student])
        i = 0
        break
if i == 1:
    print("Student not found")


