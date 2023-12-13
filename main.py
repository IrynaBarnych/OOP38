import json
#СЕРІАЛІЗАЦІЯ
data = {"name": "Varia", "age": 30, "city": ["New York", "Vinytsia"]}
json_string = json.dumps(data)
print(json_string)
#десеріалізація
json_string = json.loads(json_string)
print(data)
#запис у файли
with open('data.json', "w") as file:
    json.dump(data, file)
#зчитування
with open("data.json", 'r') as file:
    loadet_data = json.load(file)
    print(loadet_data)
#можна серіалізація списку
my_list = [1, 2, 3, 4, 5, "apple"]
json_string = json.dumps(my_list)
print(json_string)

with open('my_list.json', "w") as file:
    json.dump(my_list, file)

# Параметр indent для красивого відображення JSON
data = {1: "John", 2: 30, 3: "New York"}
json_string = json.dumps(data, indent=10, sort_keys = True)
print(json_string)


"""Серіалізація об'єктів класу у JSON:
Створіть клас, який представляє об'єкт з деякими властивостями
(наприклад, користувач з ім'ям та віком).
Серіалізуйте екземпляр цього класу в JSON за
допомогою json.dumps() та переконайтесь, що дані правильно серіалізовані."""
import json
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} {self.age}"

user = User("Alice", 30)
serialized_user = json.dumps(user.__dict__)

print(serialized_user)
load_user = json.loads(serialized_user)
print(load_user)
#user = User(load_user["name"], load_user["age"])
#user = User(**load_user)
user = User(*load_user.values())
print(user)
