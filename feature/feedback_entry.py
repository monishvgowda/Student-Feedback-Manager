
# Gets student details using input()
name = input("Enter student name: ")
age = input("Enter student age: ")
mark1 = input("Enter marks for Subject 1: ")
mark2 = input("Enter marks for Subject 2: ")
mark3 = input("Enter marks for Subject 3: ")

# Store all details in a list
student_data = [name, age, mark1, mark2, mark3]

# Print the data
print("\n--- Student Details ---")
print("Name:", student_data[0])
print("Age:", student_data[1])
print("Subject 1 Marks:", student_data[2])
print("Subject 2 Marks:", student_data[3])
print("Subject 3 Marks:", student_data[4])
