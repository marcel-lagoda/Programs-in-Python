# import typing

student_list = []


def create_student() -> dict:
    student_data = {}
    while not student_data:
        name = input("Enter student's name: ").strip().capitalize()
        if name.isalpha() and len(name) > 2:
            student_data = {"name": name, "marks": []}
            return student_data
        else:
            print("Not a valid entry. Try again.")


def add_mark(student: dict, mark: int):
    student["marks"].append(mark)


def student_avg(student: dict) -> float:
    try:
        return sum(student["marks"]) / len(student["marks"])
    except ZeroDivisionError:
        print("No marks.")


def print_student_data(student: dict):
    print(
        f"name: {student['name']}, marks: {student['marks']}, avg: {student_avg(student)}"
    )


def list_all_students(students: list):
    for idx, student in enumerate(students):
        print(f"id: {idx}, {print_student_data(student)}")


def get_student_id() -> int:
    while True:
        try:
            idx = int(input("Enter student id from the list above: "))
            return idx
        except ValueError:
            print("Only digits.")


def get_mark() -> int:
    while True:
        try:
            mark = int(input("Enter a new mark: "))
            return mark
        except ValueError:
            print("Mark invalid. Try again.")


def menu():
    # Add a student
    # Add a mark to a student
    # Print a list of students
    # Exit the application

    user_choice = input(
        "'s' to add a student,"
        "'m' to add a new mark"
        "'l' to list all students' data"
        "'q' to exit app: "
    )

    while user_choice != "q":
        if user_choice == "s":
            student_list.append(create_student())
        elif user_choice == "m":
            if student_list:
                list_all_students(student_list)
                try:
                    student_id = get_student_id()
                    student = student_list[student_id]
                    new_mark = get_mark()
                    add_mark(student, new_mark)
                except (IndexError, ValueError):
                    pass
            else:
                print("First add student.")
        elif user_choice == "l":
            list_all_students(student_list)

        user_choice = input(
            "'s' to add a student,"
            "'m' to add a new mark"
            "'l' to list all students' data"
            "'q' to exit app: "
        )


if __name__ == "__main__":
    menu()
