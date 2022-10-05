
def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            f.write(f'{s[:-1]}\n')

def write_csv(filename: str, data: list):
    with open('Seminar7_phonebook\phonebook.csv', 'w', encoding='utf-8') as f:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            f.write(f'{s[:-1]}\n')

def read_csv(filename: str) -> list:
    data = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open('Seminar7_phonebook\phonebook.csv', 'r', encoding='utf-8') as f:
        for line in f:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def find_my_name(data: list, last_name: str) -> str:
    for el in data:
        if el.get('Фамилия') == last_name:
            return el.get('Телефон')
    return 'Такой абонент отсутствует'

def find_my_number(data: list, phone_number: str) -> str:
    for el1 in data:
        if el1.get('Телефон') == phone_number:
            return el1.get('Фамилия')
    return 'Такой абонент отсутствует'

def add_user(data: list, user_data: str):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)

