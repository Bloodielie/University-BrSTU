import os
from typing import List, Callable, Dict
from pprint import pprint

Students = List[List[str]]
MenuFunc = Callable[[Students], None]


def read_data(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def convert_data_to_csv(data: str) -> Students:
    return [element.replace("\0", "").split(";") for i, element in enumerate(data.split("\n")) if i != 0]


def increase_age(students: Students) -> None:
    group = input("Enter group: ")
    for student in students:
        if student[3] == group:
            student[2] = str(int(student[2]) + 1)


def save_students_to_file(students: Students) -> None:
    path_to_file = input("Enter path to file: ")
    with open(path_to_file, "w", encoding="utf-8") as f:
        f.write("№;ФИО;Возраст;Группа\n")
        f.write("\n".join([";".join(student) for student in students]))


def receive_student_from_file(students: Students) -> None:
    path_to_file = input("Enter path to file: ")
    students.extend(convert_data_to_csv(read_data(path_to_file)))


def bad_input(_: Students) -> None:
    return print("Bad menu number")


def get_menu_func(func_mapping: Dict[str, MenuFunc]) -> Callable[[str], MenuFunc]:
    def get_menu_func_inner(num: str) -> MenuFunc:
        return func_mapping.get(num, bad_input)

    return get_menu_func_inner


def menu(students: Students, menu_text: str, get_func_callback: Callable[[str], MenuFunc]) -> None:
    while True:
        menu_number = input(menu_text)
        if menu_number == "0":
            break

        get_func_callback(menu_number)(students)
        pprint(students)


def task1() -> None:
    print("Task 1:")
    print("Files: {}".format(len(os.listdir("./test"))))


def task2() -> None:
    print("Task 2:")
    pprint(sorted(convert_data_to_csv(read_data("students.csv")), reverse=True))


def task3() -> None:
    print("Task 3:")
    students = convert_data_to_csv(read_data("students.csv"))
    return menu(
        students,
        "Menu:\n0 - Exit\n1 - Increase age by group: \n",
        get_menu_func({"1": increase_age})
    )


def task4() -> None:
    print("Task 4:")
    students = convert_data_to_csv(read_data("students.csv"))
    return menu(
        students,
        "Menu:\n0 - Exit\n1 - Increase age by group \n2 - Save students to file \n",
        get_menu_func({"1": increase_age, "2": save_students_to_file})
    )


def task5() -> None:
    print("Task 5:")
    students = convert_data_to_csv(read_data("students.csv"))
    return menu(
        students,
        "Menu:\n0 - Exit\n1 - Increase age by group \n2 - Save students to file \n3 - Get data from file\n",
        get_menu_func({"1": increase_age, "2": save_students_to_file, "3": receive_student_from_file})
    )


def main() -> None:
    task5()


if __name__ == "__main__":
    main()
