students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    dept = input("Enter department: ")
    students.append({"name": name, "roll": roll, "dept": dept})
    print("✅ Student added successfully!\n")

def view_students():
    print("\n--- Student List ---")
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Dept: {s['dept']}")
    print("--------------------\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("❌ Invalid choice, try again.\n")
