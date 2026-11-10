import csv
FILE = 'Student.csv'

def load_students():
    try:
        with open(FILE, "r", newline="") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []


def save_students(students):
    with open(FILE, "w", newline="") as f:
        fields = ["ID", "Name", "Age", "Course"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(students)


students = load_students()

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course
    }

    students.append(student)
    save_students(students)
    print("Student Added Successfully!")

def view_students():
    for student in students:
        print(student)

def update_student():
    sid = input("Enter Student ID to update: ")

    for student in students:
        if student["ID"] == sid:
            student["Name"] = input("Enter New Name: ")
            student["Age"] = input("Enter New Age: ")
            student["Course"] = input("Enter New Course: ")

            save_students(students)
            print("Student Updated Successfully!")
            return

    print("Student Not Found!")

def delete_student():
    sid = input("Enter Student ID to delete: ")

    for student in students:
        if student["ID"] == sid:
            students.remove(student)
            save_students(students)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()1

    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid Choice!")