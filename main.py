# Завдання 2
# Створіть програму для проведення опитування або
# анкетування. Зберігайте відповіді користувачів у форматі
# JSON файлу. Кожне опитування може бути окремим
# об'єктом у файлі JSON, а відповіді кожного користувача -
# списком значень.


import json

class Anketa:
    def __init__(self, name, age, hobby, location):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.location = location

def save_survey_to_json(user, filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(user.__dict__)

    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

user = Anketa("Dmytro", 30, "fishing", "Kyiv")
filename = "survey_results.json"
save_survey_to_json(user, filename)

print(f"Дякуємо за участь у опитуванні! Результати збережено у файлі {filename}.")

# або

import json

class Anketa:
    def __init__(self, name, age, hobby, location):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.location = location

def save_survey_to_json(user, filename):
    try:
        with open(filename, 'r+') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append({
        'name': user.name,
        'age': user.age,
        'hobby': user.hobby,
        'location': user.location
    })

    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

user = Anketa("Dmytro", 30, "fishing", "Kyiv")
filename = "survey_results.json"
save_survey_to_json(user, filename)

print(f"Дякуємо за участь у опитуванні! Результати збережено у файлі {filename}.")
