# Завдання 3
# До вже реалізованого класу «Стадіон» додайте можливість
# стиснення та розпакування даних з використанням json та pickle.

import pickle
import gzip
import json
class Stadium:
    def __init__(self, name, opening_date, country, city, capacity, length, width, distance_a, distance_b):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity
        self.length = length
        self.width = width
        self.distance_a = distance_a
        self.distance_b = distance_b
    def __sub__(self, other):
        return (self.capacity - other.capacity)

    def __mul__(self, other):
        square1 = self.length * self.width
        square2 = other.length * other.width
        return abs(square1 - square2)

    def __add__(self, other):
        distance1 = self.distance_a ** 2 + self.distance_b ** 2
        distance2 = other.distance_a ** 2 + other.distance_b ** 2
        return abs(distance1 - distance2)

    def to_dict(self):
        return {
            'name': self.name,
            'opening_date': self.opening_date,
            'country': self.country,
            'city': self.city,
            'capacity': self.capacity,
            'length': self.length,
            'width': self.width,
            'distance_a': self.distance_a,
            'distance_b': self.distance_b
        }

stadion1 = Stadium("Олімпійський", "22.09.1923", "Україна", "Київ", 70050,
                   150, 100, 1, 2)
stadion2 = Stadium("Донбас-Арена", "29.09.2009", "Україна", "Донецьк",  525180,
                   105, 68, 2, 3)

difference = stadion1 - stadion2
print(f"Різниця в місткості стадіонів: {difference} осіб")

area_difference = stadion1 * stadion2
print(f"Різниця в площі стадіонів: {area_difference} квадратних метрів")

plane_distance = stadion1 + stadion2
print(f"Різниця від центру міста до стадіонів: {plane_distance}")

with open('stadium_object_file.pickle', 'wb') as file:
    pickle.dump(stadion1, file)

# Збереження об'єкта у файл з використанням pickle
with open('stadium_object_file.pickle', 'wb') as file:
    pickle.dump(stadion1, file)

# Стиснення файлу з об'єктом за допомогою gzip
with open('stadium_object_file.pickle', 'rb') as file:
    data = file.read()
    with gzip.open('compressed_stadium_object_file.gz', 'wb') as compressed_file:
        compressed_file.write(data)
    print("Файл стиснуто.")

# Завантаження стиснутого файлу, розпакування та завантаження об'єкта з файлу
with gzip.open('compressed_stadium_object_file.gz', 'rb') as compressed_file:
    uncompressed_data = compressed_file.read()
    with open('uncompressed_stadium_object_file.pickle', 'wb') as file:
        file.write(uncompressed_data)
    print("Файл розпаковано.")

# Використання pickle для завантаження об'єкта з розпакованого файлу
with open('uncompressed_stadium_object_file.pickle', 'rb') as file:
    loaded_stadium = pickle.load(file)

# Збереження вкладеної структури у файл JSON
nested_data = {'stadium1': stadion1.to_dict(), 'stadium2': stadion2.to_dict()}

with open('nested_stadium_data.json', 'w') as file:
    json.dump(nested_data, file, indent=4)

# Завантаження вкладеної структури з файлу JSON для перевірки
with open('nested_stadium_data.json', 'r') as file:
    loaded_data = json.load(file)

# Відновлення об'єктів без використання @classmethod
loaded_stadium1 = Stadium(**loaded_data['stadium1'])
loaded_stadium2 = Stadium(**loaded_data['stadium2'])

# Перевірка виведення інформації про завантажений об'єкт
print(f"Назва: {loaded_stadium1.name}")
print(f"Дата відкриття: {loaded_stadium1.opening_date}")
print(f"Країна: {loaded_stadium1.country}")
print(f"Місто: {loaded_stadium1.city}")
print(f"Місткість: {loaded_stadium1.capacity}")
print(f"Довжина: {loaded_stadium1.length}")
print(f"Ширина: {loaded_stadium1.width}")
print(f"Відстань A: {loaded_stadium1.distance_a}")
print(f"Відстань B: {loaded_stadium1.distance_b}")