
import csv

students = []

def add_student():
    name = input("Enter the student's name: ")
    roll_no = input("Enter the roll number: ")
    grade = input("Enter the grade: ")
    student = {"name": name, "roll_no": roll_no, "grade": grade}
    students.append(student)
    print(f"Information for {name} has been successfully added!")


def update_student():
    roll_no = input("Enter the roll number to update: ")
    for student in students:
        if student["roll_no"] == roll_no:
            print(f"Updating information for {student['name']}.")
            student["name"] = input("Enter the new name: ")
            student["grade"] = input("Enter the new grade: ")
            print("Information has been updated!")
            return
    print("Roll number not found.")


def delete_student():
    roll_no = input("Enter the roll number to delete: ")
    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print(f"Information for {student['name']} has been deleted.")
            return
    print("Roll number not found.")


def list_students():
    if not students:
        print("The student list is empty.")
    else:
        print("List of students:")
        for i, student in enumerate(students, start=1):
            print(f"{i}. Name: {student['name']}, Roll Number: {student['roll_no']}, Grade: {student['grade']}")


def search_student():
    roll_no = input("Enter the roll number to search: ")
    for student in students:
        if student["roll_no"] == roll_no:
            print(f"Found! Name: {student['name']}, Grade: {student['grade']}")
            return
    print("Roll number not found.")


def save_to_csv():
    filename = input("Enter the CSV file name (e.g., students.csv): ")
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "roll_no", "grade"])
        writer.writeheader()
        writer.writerows(students)
    print(f"Data has been saved to {filename}!")


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add a student")
        print("2. Update a student")
        print("3. Delete a student")
        print("4. View the list of students")
        print("5. Search for a student")
        print("6. Save data to a CSV file")
        print("7. Exit")
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            list_students()
        elif choice == "5":
            search_student()
        elif choice == "6":
            save_to_csv()
        elif choice == "7":
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
     main()




















