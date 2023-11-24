
students = []
num_students = int(input("Enter the number of students: "))

# Get the details of each student
for i in range(num_students):
    name = input("Enter the name of student " + str(i+1) + ": ")
    rollno = int(input("Enter the roll number of student " + str(i+1) + ": "))
    marks = int(input("Enter the total marks (out of 100) of student " + str(i+1) + ": "))
    
    # Add the student record to the list
    students.append({"name": name, "rollno": rollno, "marks": marks})

# Find the student with maximum marks
max_marks_student = max(students, key=lambda student: student['marks'])

# Display the details of the student with maximum marks
print("The student with maximum marks is:")
print("Name:", max_marks_student['name'])
print("Roll Number:", max_marks_student['rollno'])
print("Marks:", max_marks_student['marks'])
