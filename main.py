# Завдання 4
# До вже реалізованого класу «Годинник» додайте
# мож-ливість стиснення та розпакування даних з
# використан-ням json та pickle.

import pickle
import gzip
import json

class Watch:
    def __init__(self, model, manufacturer, year, price, watch_type):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.watch_type = watch_type

    def get_model(self):
        return self.model

    def get_manufacturer(self):
        return self.manufacturer

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price

    def get_watch_type(self):
        return self.watch_type

    def __sub__(self, other):
        return abs(self.price - other.price)

    def is_same_watch_type(self, other):
        return self.watch_type == other.watch_type

    def to_dict(self):
        return {
            'model': self.get_model(),
            'manufacturer': self.get_manufacturer(),
            'year': self.get_year(),
            'price': self.get_price(),
            'watch_type': self.get_watch_type()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            model=data['model'],
            manufacturer=data['manufacturer'],
            year=data['year'],
            price=data['price'],
            watch_type=data['watch_type']
        )

# Створення об'єктів
watch1 = Watch("Чип", "Швейцарія", 2020, 200, "Ручний")
watch2 = Watch("Дейл", "Китай", 2022, 300, "Настінний")

# Збереження об'єкта у файл з використанням pickle
with open('object_file.pickle', 'wb') as file:
    pickle.dump(watch1, file)

# Стиснення файлу з об'єктом за допомогою gzip
with open('object_file.pickle', 'rb') as file:
    data = file.read()
    with gzip.open('compressed_object_file.gz', 'wb') as compressed_file:
        compressed_file.write(data)
    print("Файл стиснуто.")

# Завантаження стиснутого файлу, розпакування та завантаження об'єкта з файлу
with gzip.open('compressed_object_file.gz', 'rb') as compressed_file:
    uncompressed_data = compressed_file.read()
    with open('uncompressed_object_file.pickle', 'wb') as file:
        file.write(uncompressed_data)
    print("Файл розпаковано.")

# Використання pickle для завантаження об'єкта з розпакованого файлу
with open('uncompressed_object_file.pickle', 'rb') as file:
    loaded_watch = pickle.load(file)

# Збереження вкладеної структури у файл JSON
nested_data = {'fraction1': watch1.to_dict(), 'fraction2': watch2.to_dict()}

with open('nested_data.json', 'w') as file:
    json.dump(nested_data, file, indent=4)

# Завантаження вкладеної структури з файлу JSON для перевірки
with open('nested_data.json', 'r') as file:
    loaded_data = json.load(file)

loaded_watch1 = Watch.from_dict(loaded_data['fraction1'])
loaded_watch2 = Watch.from_dict(loaded_data['fraction2'])

# Перевірка виведення інформації про завантажений об'єкт
print(f"Модель: {loaded_watch1.get_model()}")
print(f"Виробник: {loaded_watch1.get_manufacturer()}")
print(f"Рік випуску: {loaded_watch1.get_year()}")
print(f"Ціна: {loaded_watch1.get_price()}")
print(f"Вид годинника: {loaded_watch1.get_watch_type()}")
