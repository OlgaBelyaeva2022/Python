def show_menu() -> int:
    print('\nВыберите необходимое действие:\n'
            '1. Отобразить весь список сотрудников\n'
            '2. Найти сотрудника по фамилии\n'
            '3. Сделать выборку сотрудников по зарплате\n'
            '4. Добавить сотрудника\n'
            '5. Удалить сотрудника\n'
            '6. Экспортировать данные в формате json\n'
            '7. Закончить работу\n')

    choice = int(input())
    return choice

def print_result(data: list):
    for el in data:
        s = ''
        for v, k in el.items():
            s += f'{v}: {k}\n'
        print(s)

def get_search_name() -> str:
    return input('Введите фамилию для поиска: ')

def get_new_employee() -> str:
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    position = input('Введите должность сотрудника: ')
    salary = input('Введите заработную плату сотрудника: ')
    return f'{last_name}, {first_name}, {phone_number}, {position}, {salary}'


def get_salary_range():
    start = float(input('Введите начало диапозона значений: '))
    end = float(input('Введите конец диапозона значений: '))
    return start, end

def show_employee_info(data: dict):
    for k, v in data.items():
        print(f'{k}: {v}')


