from funcs import get_welcome_msg
import os

def welcome_all_employees_in_file(file_path):
    # read the employee names from a file
    with open(file_path) as file:
        employees = file.read().splitlines()

    number_of_employees = len(employees)
    for i in range(number_of_employees):
        employee_name, role = employees[i].split(',')

        msg = get_welcome_msg(employee_name, role)
        print(msg)


# get path of this file

folder_path = os.path.dirname(__file__)

print(folder_path)

welcome_all_employees_in_file(os.path.join(folder_path, "employees.txt"))
print("*************************************")
welcome_all_employees_in_file(os.path.join(folder_path, "employees2.txt"))
