student_list = []


def add_student():
    """
    Add a new student.
    :return: dict of student data
    """
    # student_data = {}
    while True:
        name = input("Please enter a student's name: ").capitalize().strip()
        if len(name) < 1:
            print("This value cannot be empty. Please enter a student name.")
        elif not name.isalpha():
            print("This value cannot be a number. Only letters.")
        elif name.isalpha():
            student_data = {
                "name": name,
                "marks": [],
            }

            return student_data


def add_mark(student, mark):
    student["marks"].append(mark)
    # print(type(student))
    # return student


def calculate_average_mark(student):
    number = len(student["marks"])
    if number == 0:
        return 0

    total = sum(student["marks"])
    return total / number


def print_student_details(student):
    print(f"{student['name']}, average mark: {calculate_average_mark(student)}.")


def print_student_list(students):
    for i, student in enumerate(students):
        print(f"ID: {i}")
        print_student_details(student)


def menu():
    selection = input(
        "Enter 'p' to print the student list, "
        "'s' to add a new student, "
        "'m' to add a mark to a student, "
        "or 'q' to quit. "
        "Enter your selection: "
    )
    # skąd wie, że ma zakończyć?

    while selection.lower() != "q":
        if selection.lower() == "p":
            print_student_list(student_list)
        elif selection.lower() == "s":
            student_list.append(add_student())
        elif selection.lower() == "m":
            print_student_list(student_list)
            student_id = int(input("Enter the student ID to add a mark to: "))
            if student_id > len(student_list):
                print("There is no student with such #ID. Please add a student first!")
                student_list.append(add_student())
                while True:
                    try:
                        print_student_list(student_list)
                        student_id = int(
                            input("Enter the student ID to add a mark to: ")
                        )
                        student = student_list[student_id]
                        new_mark = int(input("Enter x the new mark to be added: "))
                        add_mark(student, new_mark)
                        break
                    except ValueError:
                        print("Only digits allowed")
            else:
                new_mark = int(input("Enter the new mark to be added: "))
                add_mark(student, new_mark)

        selection = input(
            "Enter 'p' to print the student lista, "
            "'s' to add a new student, "
            "'m' to add a mark to a student, "
            "or 'q' to quit. "
            "Enter your selection: "
        )


menu()
