
# Lab 15 - Student Information Management System

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


def display_students():
    """Display all enrolled student records."""
    print("\n--- Enrolled Student Records ---")

    if not students:
        print("No student records available.")
        return

    for roll, details in students.items():
        print(
            f"Roll No: {roll} | "
            f"Name: {details['Name']} | "
            f"Branch: {details['Branch']} | "
            f"Sem: {details['Semester']} | "
            f"Marks: {details['Marks']}"
        )

    print("Total Enrolled Students:", len(students))


def search_student():
    """Search for a student using their roll number."""
    roll = input("Enter Roll Number to search: ").strip()

    student = students.get(roll)

    if student:
        print(f"\n[FOUND] Record for Roll No {roll}:")
        print("Name     :", student["Name"])
        print("Branch   :", student["Branch"])
        print("Semester :", student["Semester"])
        print("Marks    :", student["Marks"])
    else:
        print("[ERROR] Student record not found.")


def register_student():
    """Register a new student with a unique roll number."""
    print("\n--- Register New Student ---")

    roll = input("Enter Roll Number: ").strip()

    if not roll:
        print("[ERROR] Roll number cannot be empty.")
        return

    if roll in students:
        print("[ERROR] Roll Number already exists.")
        return

    name = input("Enter Student Name: ").strip()
    branch = input("Enter Branch (e.g. BCA AI): ").strip()
    semester = input("Enter Semester: ").strip()

    if not name or not branch or not semester:
        print("[ERROR] Student details cannot be empty.")
        return

    marks = []

    for i in range(3):
        while True:
            try:
                mark = int(input(f"Subject {i + 1}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid integer.")

    students[roll] = {
        "Name": name,
        "Branch": branch,
        "Semester": semester,
        "Marks": marks
    }

    print(
        f"\n[SUCCESS] Student '{name}' "
        f"(Roll No: {roll}) registered successfully."
    )


def update_student():
    """Update a student's branch or semester."""
    roll = input("Enter Roll Number to update: ").strip()

    student = students.get(roll)

    if student is None:
        print("[ERROR] Student record not found.")
        return

    print(
        f"\nCurrent details for {student['Name']} "
        f"(Roll {roll}):"
    )
    print("1. Branch:", student["Branch"])
    print("2. Semester:", student["Semester"])

    choice = input(
        "Choose field to update (1 for Branch, 2 for Semester): "
    ).strip()

    if choice == "1":
        new_branch = input("Enter new branch: ").strip()

        if new_branch:
            student["Branch"] = new_branch
            print(
                f"[SUCCESS] Branch updated to '{new_branch}'."
            )
        else:
            print("[ERROR] Branch cannot be empty.")

    elif choice == "2":
        new_semester = input("Enter new semester: ").strip()

        if new_semester:
            student["Semester"] = new_semester
            print(
                f"[SUCCESS] Semester updated to "
                f"'{new_semester}'."
            )
        else:
            print("[ERROR] Semester cannot be empty.")

    else:
        print("[ERROR] Invalid field choice.")


def academic_performance():
    """Calculate total marks, average, and pass/fail status."""
    roll = input(
        "Enter Roll Number for Academic Performance: "
    ).strip()

    student = students.get(roll)

    if student is None:
        print("[ERROR] Student record not found.")
        return

    marks = student["Marks"]
    total = sum(marks)
    average = total / len(marks)

    # Passing threshold: average percentage >= 40%
    if average >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    print("\n" + "=" * 20 + " ACADEMIC REPORT " + "=" * 20)
    print(f"Student Name : {student['Name']} (Roll: {roll})")
    print("Subject Marks:", marks)
    print(f"Total Marks  : {total} / {len(marks) * 100}")
    print(f"Average Marks: {average:.2f}%")
    print(f"Final Result : {result}")
    print("=" * 57)


def delete_student():
    """Delete a student record safely."""
    roll = input("Enter Roll Number to delete: ").strip()

    student = students.pop(roll, None)

    if student is not None:
        print(
            f"\n[SUCCESS] Record for '{student['Name']}' "
            f"(Roll No: {roll}) deleted successfully."
        )
    else:
        print("[ERROR] Student record not found.")


# Main menu
while True:
    print("\n" + "=" * 12 + " STUDENT INFORMATION MANAGEMENT SYSTEM " + "=" * 12)
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ").strip()

    if choice == "1":
        display_students()

    elif choice == "2":
        search_student()

    elif choice == "3":
        register_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        academic_performance()

    elif choice == "6":
        delete_student()

    elif choice == "7":
        print("\nThank you for using the Student Management System. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 7.")
