import csv

# Read Student Results
def read_results():
    students = []

    try:
        with open("results.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students.append({
                    "usn": row["USN"].strip(),
                    "name": row["Name"].strip(),
                    "percentage": float(row["Percentage"]),
                    "result": row["Result"].strip().upper()
                })

    except FileNotFoundError:
        print("Error: results.csv file not found!")
        return []

    return students

# Display Top 10 Toppers
def top_toppers(students):
    passed = [s for s in students if s["result"] == "PASS"]

    toppers = sorted(
        passed,
        key=lambda x: x["percentage"],
        reverse=True
    )[:10]

    print("\n===== TOP 10 TOPPERS =====")

    for i, student in enumerate(toppers, start=1):
        print(i, student["name"], "-", student["percentage"], "%")

# Display First Class Students
def first_class(students):
    print("\n===== FIRST CLASS STUDENTS =====")

    found = False

    for s in students:
        if s["result"] == "PASS" and s["percentage"] >= 60:
            print(s["name"], "-", s["percentage"], "%")
            found = True

    if not found:
        print("No students found.")

# Display Second Class Students
def second_class(students):
    print("\n===== SECOND CLASS STUDENTS =====")

    found = False

    for s in students:
        if s["result"] == "PASS" and 50 <= s["percentage"] < 60:
            print(s["name"], "-", s["percentage"], "%")
            found = True

    if not found:
        print("No students found.")

# Display Failed Students
def failed_students(students):
    print("\n===== FAILED STUDENTS =====")

    found = False

    for s in students:
        if s["result"] == "FAIL":
            print(s["name"], "-", s["percentage"], "%")
            found = True

    if not found:
        print("No failed students.")

# Display Result Statistics
def result_statistics(students):
    total = len(students)

    passed = sum(1 for s in students if s["result"] == "PASS")
    failed = sum(1 for s in students if s["result"] == "FAIL")

    print("\n===== RESULT STATISTICS =====")
    print("Total Students:", total)
    print("Passed Students:", passed)
    print("Failed Students:", failed)

    if total > 0:
        print("Pass Percentage:", round(passed / total * 100, 2), "%")
        print("Failure Percentage:", round(failed / total * 100, 2), "%")

# Display All Students
def display_all(students):
    print("\n===== ALL STUDENTS =====")

    for s in students:
        print(
            s["usn"],
            s["name"],
            s["percentage"],
            s["result"]
        )

# Fetch Individual Student Result (Only PASS / FAIL)
def individual_result(students):
    print("\n===== INDIVIDUAL STUDENT RESULT =====")

    usn = input("Enter Student USN: ").strip().upper()

    found = False

    for s in students:
        if s["usn"].upper() == usn:
            print("\n===== STUDENT RESULT =====")
            print("Result:", s["result"])
            found = True
            break

    if not found:
        print("Student USN not found!")

# Main Menu
def main():
    students = read_results()

    if not students:
        print("No student data available.")
        return

    while True:
        print("\n================================")
        print("       VTU RESULT ANALYZER")
        print("================================")
        print("1. Top 10 Toppers")
        print("2. First Class Students")
        print("3. Second Class Students")
        print("4. Failed Students")
        print("5. Result Statistics")
        print("6. Display All Students")
        print("7. Individual Student Result")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            top_toppers(students)

        elif choice == "2":
            first_class(students)

        elif choice == "3":
            second_class(students)

        elif choice == "4":
            failed_students(students)

        elif choice == "5":
            result_statistics(students)

        elif choice == "6":
            display_all(students)

        elif choice == "7":
            individual_result(students)

        elif choice == "8":
            print("Thank you for using VTU Result Analyzer!")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()