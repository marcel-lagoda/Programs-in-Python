students_list = []


def create_student():
    while True:
        name = input("Please enter a student's name: ").capitalize().strip()
        if len(name) < 1:
            print("This value cannot be empty. Please enter a student name.")
        elif not name.isalpha():
            print("This value cannot be a number. Only letters.")
        elif name.isalpha():
            student_data = {"name": name, "marks": []}

            return student_data


# def add_student():
#     student_data = {}
#     while not student_data:
#         name = input("Enter a student name: ").strip().capitalize()
#         if len(name) > 0 and name.isalpha():
#             student_data = {"name": name, "marks": []}
#         else:
#             print("Try again:")
#     return student_data


def add_mark(student, mark):
    student["marks"].append(mark)


def calculate_student_avg(student):
    try:
        result = sum(student["marks"]) / len(student["marks"])
        return result
    except ZeroDivisionError:
        return


def print_student_details(student):
    print(f'{student["name"]}, average: {calculate_student_avg(student)}')


def print_all_students(students):
    for idx, student in enumerate(students):
        print(f"ID: {idx}, {print_student_details(student)}")


def menu():
    choice = input(
        "Enter 'p' to print all students,"
        "'s' to add a new student,"
        "'m' to add a new mark to a student,"
        "'q' to end program."
        "Select your choice: "
    )

    while choice != "q":
        if choice == "p":
            print_all_students(students_list)
        elif choice == "s":
            students_list.append(create_student())
        elif choice == "m":
            if students_list:
                print_all_students(students_list)
                try:
                    student_id = int(input("Select the student ID to add a mark to: "))
                    student = students_list[student_id]
                    new_mark = int(input("Enter the new mark to be added: "))
                    add_mark(student, new_mark)
                except (IndexError, ValueError):
                    pass

        choice = input(
            "Enter 'p' to print all students,"
            "'s' to add a new student,"
            "'m' to add a new mark to a student,"
            "'q' to end program."
            "Select your choice: "
        )


menu()
