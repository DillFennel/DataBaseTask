"""
29 Вариант

Данные:
Название детали (ключ)
Тип детали
Количество на складе

Индивидуальное задание:
Агрегировать данные по второму полю.
Вывести на экран информацию вида (2 поле) – (количество элементов) – (среднее значение поля 3)
"""

class Detail:
    name = None
    detail_type = None
    quantity = None

    def __init__(self, name=None, detail_type=None, quantity=None):
        self.name = name
        self.detail_type = detail_type
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} {self.detail_type} {self.quantity}"

    def from_list(self, a):
        self.name = a[0]
        self.detail_type = a[1]
        self.quantity = int(a[2])

    def to_list(self):
        return [self.name, self.detail_type, str(self.quantity)]

    def print(self):
        print(f"{self.name}, {self.detail_type}, {self.quantity}")

details = []

def print_details():
    print('\nСписок деталей:')
    for detail in details:
        print(detail)

def add_detail():
    print('\nДобавление новой детали')
    name = input("Введите название детали: ")
    detail_type = input("Введите тип детали: ")
    quantity = int(input("Введите количество: "))
    detail = Detail(name, detail_type, quantity)
    details.append(detail)
    print("Деталь добавлена")

def load_from_csv():
    print('\nЗагрузка из файла CSV')
    filename = input("Введите имя файла (например: details.csv): ")
    try:
        details.clear()
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for row in lines:
                data = row.strip().split(";")
                if len(data) == 3:
                    detail = Detail()
                    detail.from_list(data)
                    details.append(detail)
        print("Данные успешно загружены")
    except Exception as e:
        print(f"Ошибка: {e}")

def save_to_csv():
    print('\nСохранение в файл CSV')
    filename = input("Введите имя файла (например: details.csv): ")
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for detail in details:
                f.write(';'.join(detail.to_list())+'\n')
        print("Данные сохранены в", filename)
    except Exception as e:
        print(f"Ошибка: {e}")

def find_by_name():
    print('\nПоиск детали по названию')
    name = input("Введите название детали: ")
    found = False
    for detail in details:
        if detail.name.lower() == name.lower():
            print("Найдена деталь:", detail)
            found = True
    if not found:
        print("Деталь с таким названием не найдена")

def delete_by_name():
    print('\nУдаление детали по названию')
    name = input("Введите название детали: ")
    found = 0
    for i in range(len(details)-1, -1, -1):
        if details[i].name.lower() == name.lower():
            details.pop(i)
            found += 1
    print("Удалено записей: ", found)

def aggregate_by_type():
    print('\nАгрегация данных по типу детали:')
    type_stats = {}
    for detail in details:
        if detail.detail_type not in type_stats:
            type_stats[detail.detail_type] = {
                'count': 0,
                'total_quantity': 0
            }
        type_stats[detail.detail_type]['count'] += 1
        type_stats[detail.detail_type]['total_quantity'] += detail.quantity
    print("Тип детали - Количество элементов - Среднее количество")
    for detail_type, stats in type_stats.items():
        avg_quantity = stats['total_quantity'] / stats['count']
        print(f"{detail_type} - {stats['count']} - {avg_quantity:.2f}")

while True:
    print('\nСписок действий:')
    print('1 - Загрузка базы из файла CSV')
    print('2 - Сохранение базы в файл CSV')
    print('3 - Вывод всех деталей на экран')
    print('4 - Добавление новой детали')
    print('5 - Поиск детали по названию')
    print('6 - Удаление детали по названию')
    print('7 - Агрегация данных по типу детали')
    print('0 - Выход')
    cmd = int(input('Выберите команду: '))
    if cmd == 1:
        load_from_csv()
    elif cmd == 2:
        save_to_csv()
    elif cmd == 3:
        print_details()
    elif cmd == 4:
        add_detail()
    elif cmd == 5:
        find_by_name()
    elif cmd == 6:
        delete_by_name()
    elif cmd == 7:
        aggregate_by_type()
    elif cmd == 0:
        print("Выход из программы")
        break
    else:
        print("Неверная команда. Попробуйте снова.")