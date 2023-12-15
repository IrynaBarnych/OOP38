# Завдання 3
# До вже реалізованого класу «Дріб» додайте можливість стиснення та розпакування даних з
# використанням json та pickle.


import json
import pickle
import gzip

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        other.denominator, other.numerator = other.numerator, other.denominator
        return Fraction.__mul__(self, other)

    def display_info(self):
        print(f"Дріб: {self.numerator}/{self.denominator}")

# Решта коду залишається незмінною

fraction1 = Fraction(4, 7)
fraction2 = Fraction(5, 8)

print(f"Додавання: {fraction1 + fraction2}")
print(f"Віднімання: {fraction1 - fraction2}")
print(f"Множення: {fraction1 * fraction2}")
print(f"Ділення: {fraction1 / fraction2}")

# Збереження об'єкта у файл з використанням pickle
with open('object_file.pickle', 'wb') as file:
    pickle.dump(fraction1, file)

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
    loaded_obj = pickle.load(file)

# Збереження вкладеної структури у файл JSON
nested_data = {'fraction1': str(fraction1), 'fraction2': str(fraction2)}

with open('nested_data.json', 'w') as file:
    json.dump(nested_data, file, indent=4)

# Завантаження вкладеної структури з файлу JSON для перевірки
with open('nested_data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data)

# Виведення інформації про завантажений об'єкт
loaded_obj.display_info()