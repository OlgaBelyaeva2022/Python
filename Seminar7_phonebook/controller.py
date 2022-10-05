from view import (show_menu, print_result, get_search_name, get_search_number, get_new_user, get_file_name)
from model import write_txt, write_csv, read_csv, find_my_name, find_my_number, add_user


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('Seminar7_phonebook\phonebook.csv')
    
    while (choice != 6):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print(find_my_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print(find_my_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv('Seminar7_phonebook\phonebook.csv', phone_book)
        elif choice == 5:
            file_name = get_file_name()
            add_user(phone_book, user_data)
            write_txt(file_name, phone_book)
        choice = show_menu()
