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

