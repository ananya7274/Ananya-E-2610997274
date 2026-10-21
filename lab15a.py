
# Lab 15 - Student Information Management System

# Initial student records
students = {
    "101": {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [92, 88, 95]
    },
    "103": {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [74, 80, 82]
    }
}

while True:
    print("\n" + "=" * 50)
    print("       STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("=" * 50)

    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ").strip()

    # 1. View all students
    if choice == "1":
        print("\n--- Enrolled Student Records ---")

        if not students:
            print("No student records found.")
        else:
            for roll_no, details in students.items():
                print(
                    f"Roll No: {roll_no} | "
                    f"Name: {details['Name']} | "
                    f"Branch: {details['Branch']} | "
                    f"Sem: {details['Semester']} | "
                    f"Marks: {details['Marks']}"
                )

            print(f"Total Enrolled Students: {len(students)}")

    # 2. Search student by roll number
    elif choice == "2":
        roll_no = input("Enter Roll Number to search: ").strip()

        student = students.get(roll_no)

        if student:
            print(f"\n[FOUND] Record for Roll No {roll_no}:")
            print(f"  Name     : {student['Name']}")
            print(f"  Branch   : {student['Branch']}")
            print(f"  Semester : {student['Semester']}")
            print(f"  Marks    : {student['Marks']}")
        else:
            print(f"[ERROR] No student found with Roll No {roll_no}.")

    # 3. Register new student
    elif choice == "3":
        print("\n--- Register New Student ---")

        roll_no = input("Enter Roll Number: ").strip()

        if roll_no in students:
            print("[ERROR] Roll Number already exists.")
            continue

        name = input("Enter Student Name: ").strip()
        branch = input("Enter Branch (e.g. BCA AI): ").strip()
        semester = input("Enter Semester: ").strip()

        marks = []

        try:
            print("Enter marks obtained in 3 subjects:")
            for i in range(1, 4):
                mark = int(input(f"  Subject {i}: "))

                if mark < 0 or mark > 100:
                    raise ValueError("Marks must be between 0 and 100.")

                marks.append(mark)

        except ValueError as error:
            print(f"[ERROR] Invalid marks: {error}")
            continue

        if not name or not branch or not semester:
            print("[ERROR] Student details cannot be empty.")
            continue

        students[roll_no] = {
            "Name": name,
            "Branch": branch,
            "Semester": semester,
            "Marks": marks
        }

        print(
            f"\n[SUCCESS] Student '{name}' (Roll No: {roll_no}) "
            "registered successfully."
        )

    # 4. Update student details
    elif choice == "4":
        print("\n--- Update Student Details ---")

        roll_no = input("Enter Roll Number to update: ").strip()

        if roll_no not in students:
            print(f"[ERROR] No student found with Roll No {roll_no}.")
            continue

        student = students[roll_no]

        print("Leave a field blank to keep its current value.")

        new_name = input(f"Enter new name [{student['Name']}]: ").strip()
        new_branch = input(
            f"Enter new branch [{student['Branch']}]: "
        ).strip()
        new_semester = input(
            f"Enter new semester [{student['Semester']}]: "
        ).strip()

        if new_name:
            student["Name"] = new_name

        if new_branch:
            student["Branch"] = new_branch

        if new_semester:
            student["Semester"] = new_semester

        print("[SUCCESS] Student details updated.")

    # 5. View academic performance
    elif choice == "5":
        print("\n--- Academic Performance ---")

        roll_no = input("Enter Roll Number: ").strip()

        if roll_no not in students:
            print(f"[ERROR] No student found with Roll No {roll_no}.")
            continue

        student = students[roll_no]
        marks = student["Marks"]

        total = sum(marks)
        percentage = total / len(marks)

        if all(mark >= 40 for mark in marks):
            result = "PASS"
        else:
            result = "FAIL"

        print(f"\nStudent Name : {student['Name']}")
        print(f"Roll Number  : {roll_no}")
        print(f"Marks        : {marks}")
        print(f"Total Marks  : {total} / {len(marks) * 100}")
        print(f"Percentage   : {percentage:.2f}%")
        print(f"Average      : {percentage:.2f}")
        print(f"Result       : {result}")

    # 6. Delete student record
    elif choice == "6":
        print("\n--- Delete Student Record ---")

        roll_no = input("Enter Roll Number to delete: ").strip()

        student = students.pop(roll_no, None)

        if student:
            print(
                f"[SUCCESS] Student '{student['Name']}' "
                f"(Roll No: {roll_no}) deleted."
            )
        else:
            print(f"[ERROR] No student found with Roll No {roll_no}.")

    # 7. Exit
    elif choice == "7":
        print("\nThank you for using the Student Information System. Goodbye!")
        break

    # Invalid menu choice
    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 7.")
