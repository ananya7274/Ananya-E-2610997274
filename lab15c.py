
def academic_performance():
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

    result = "PASS" if average >= 40 else "FAIL"

    print("\n" + "=" * 16 + " ACADEMIC REPORT " + "=" * 16)
    print(f"Student Name : {student['Name']} (Roll: {roll})")
    print(f"Subject Marks: {marks}")
    print(f"Total Marks  : {total} / {len(marks) * 100}")
    print(f"Average Marks: {average:.2f}%")
    print(f"Final Result : {result}")
    print("=" * 56)
