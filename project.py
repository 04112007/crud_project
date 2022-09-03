import shelve
from datetime import datetime

from settings import FILENAME


def create_data():
    id_ = datetime.now().strftime('%H%M%S')
    title = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    description = input('Введите описание: ')
    created_at = datetime.now().strftime('%d.%m.%y %H:%M')
    with shelve.open(FILENAME) as db:
        db[id_] = {
            'title': title,
            'price': price,
            'description': description,
            'created_at': created_at,
        }


def get_all_data():
    with shelve.open(FILENAME) as db:
        for key, value in db.items():
            print('id:', key, '||', 'title:', value['title'], '||', 'price:', value['price'], '||', 'description:', value['description'], '||', 'created_at:', value['created_at'])


def get_data_by_id():
    id_ = input('Введите id товара: ')
    with shelve.open(FILENAME) as db:
        try:
            prod = db[id_]
            print(
                f"""
                Название: {prod['title']}
                Цена: {prod['price']}
                Описание: {prod['description']}
                статус: {prod['status']}
                Время создания: {prod['created_at']}
                """
            )
        except KeyError:
            print(f'{id_} не существует')


def update_data():
    id_ = input('Введите  id товара: ')
    with shelve.open(FILENAME, writeback=True) as db:
        try:
            prod = db[id_]
            prod['title'] = input('Введите новое название: ') or prod['title']
            prod['price'] = int(input('Введите новую цену: ')) or prod['price']
            prod['description'] = input('Введите новое описание: ') or prod['description']
            prod['status'] = input('Введите новый статус: ') or prod['status']
        except KeyError:
            print(f'{id_} не существует')


def delete_data():
    id_ = input('Введите id товара: ')
    with shelve.open(FILENAME) as db:
        try:
            db.pop(id_)
        except KeyError:
            print(f'{id_} такого id не существует')


def interface():
    info_data = """
    0) Список функций:
    1) create - создать продукт
    2) delete - удалить продукт по id
    3) update - изменить данные
    4) get by id - получить продукт по id
    5) get all - показать список всех продуктов
    6) exit - выйти из программы
    """
    print(info_data)
    while True:
        name = input()
        if name == '0':
            print(info_data)
        elif name == '1':
            create_data()
        elif name == '2':
            delete_data()
        elif name == '3':
            update_data()
        elif name == '4':
            get_data_by_id()
        elif name == '5':
            get_all_data()
        elif name == '6':
            break
        else:
            print('Функции с таким номером нет!')
            break

        



