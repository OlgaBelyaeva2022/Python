import json
import csv
from pathlib import Path
from view import (get_new_employee, get_salary_range, show_employee_info)


def write_csv(filename: str, database: list):
    with open('Seminar8\database.csv', 'w', encoding='utf-8') as f:
        for i in range(len(database)):
            s = ''
            for v in database[i].values():
                s += v + ','
            f.write(f'{s[:-1]}\n')

def read_csv():
    data = []
    with open(Path.cwd() / 'Seminar8\database.csv', 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            temp = {}
            temp['Фамилия'] = row[0]
            temp['Имя'] = row[1]
            temp['Телефон'] = row[2]
            temp['Должность'] = row[3]
            temp['Заработная плата'] = float(row[4])
            data.append(temp)
    return data


def read_json():
    employee = []
    with open('Seminar8\database1.json', 'r', encoding='utf-8') as f:
        for line in f:
            temp = json.loads(line)
            employee.append(temp)
    return employee

def write_json(database: list):
    with open('Seminar8\database1.json', 'w', encoding='utf-8') as f:
        for employee in database:
            f.write(json.dumps(employee) + '\n')

def find_my_name(database: list, last_name: str) -> str:
    for el in database:
        if el.get('Фамилия') == last_name:
            return el.get('Телефон')
    return 'Такой сотрудник отсутствует'

def add_employee(database: list, user_data: str):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Должность', 'Заработная плата']
    record = dict(zip(fields, user_data.split(',')))
    database.append(record)

def del_employee(database: list, employee: dict):
    database.remove(employee)
    

def find_employees_by_salary_range(database: list):
    result = []
    start, end = get_salary_range()
    for employee in database:
        if start <= employee['Заработная плата'] <= end:
            result.append(employee)
    return result




