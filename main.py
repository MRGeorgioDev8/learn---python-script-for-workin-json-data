import json

class DataCountry:
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        try:
            with open('data.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open('data.json', 'w') as file:
            json.dump(self.data, file, indent=2)

    def add_country(self, country, capital):
        entry = {'Country': country, 'Capital': capital}
        self.data.append(entry)
        self.save_data()

    def delete_country(self, country):
        for entry in self.data:
            if entry['Country'] == country:
                self.data.pop(self.data.index(entry))
                self.save_data()
                return

    def search_country(self, country):
        for entry in self.data:
            if entry['Country'] == country:
                return entry['Capital']
        else:
            return "Страна не найдена"

    def edit_country(self, old_country, edit_country, edit_capital):
        for entry in self.data:
            if entry['Country'] == old_country:
                entry['Country'] = edit_country
                entry['Capital'] = edit_capital
                self.save_data()
                return

    def view_data(self):
        return self.data

def input_add_country(data_input):
    country = input("Введите название страны (с заглавной буквы): ")
    capital = input("Введите название столицы страны (с заглавной буквы): ")
    data_input.add_country(country, capital)
    print("Данные сохранены")

def input_del_country(data_input):
    country = input("Введите название страны для удаления: ")

    if data_input.search_country(country):
        data_input.delete_country(country)
        print("Данные удалены")
    else:
        print("Данные не найдены. Удаление не выполнено.")

def search_input_country(data_input):
    country = input("Введите название страны для поиска: ")
    result = data_input.search_country(country)
    if result:
        print(f"{country}: {result}")
    else:
        print("Данные не найдены")

def edit_input_country(data_input):
    old_country = input("Введите название страны для редактирования: ")
    edit_country = input("Введите новое название страны (с заглавной буквы): ")
    edit_capital = input("Введите новое название столицы страны (с заглавной буквы): ")
    data_input.edit_country(old_country, edit_country, edit_capital)
    print("Данные обновлены")


def view_input_data(data_input):
    data = data_input.view_data()
    if data:
        for entry in data:
            print(f"{entry['Country']}: {entry['Capital']}")
    else:
        print("Нет данных")

saved_data = DataCountry().load_data()
data_input = DataCountry()

command = {
    '1': input_add_country,
    '2': input_del_country,
    '3': search_input_country,
    '4': edit_input_country,
    '5': view_input_data,
}

while True:
    print("*" * 30)
    print("Введите команду:")
    print("1 - добавление данных")
    print("2 - удаление данных")
    print("3 - поиск данных")
    print("4 - редактирование данных")
    print("5 - просмотр данных")
    output = input("Ввод: ")
    if output in command:
        command[output](data_input)
    else:
      print("Неверная команда. Выберите команду (1 - 5)")