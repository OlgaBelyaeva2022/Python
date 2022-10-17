from view import (show_menu, print_result, get_search_name, get_new_employee, get_file_name, get_salary_range, show_employee_info)
from model import write_csv, read_csv, find_my_name, add_employee, del_employee, write_json, read_json, find_employees_by_salary_range

def work_with_database():
    choice = show_menu()
    database = read_csv()
    
    while (choice != 7):
        if choice == 1:
            print_result(database)
        elif choice == 2:
            name = get_search_name()
            print(find_my_name(database, name))
        elif choice == 3:
            by_salary = find_employees_by_salary_range(database)
            for sal in by_salary:
                show_employee_info(sal)
        elif choice == 4:
            user_data = get_new_employee()
            add_employee(database, user_data)
            write_csv('Seminar8\database.csv', database)
        elif choice == 5:
            fired_employee = get_new_employee()
            del_employee(database, fired_employee)
        elif choice == 6:
            write_json(database)
        choice = show_menu()
