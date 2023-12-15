"""Завдання 2
Реалізація програми для додавання, видалення та
відстеження завдань. Зберігати ці завдання у
форматі JSON у файлі. Можливість завантаження
раніше збережених завдань для подальшої роботи з
ними."""

import json
import time

task = {}

def load_task():
    try:
        with open("task.json", "r") as file:
            task_data = json.load(file)
    except FileNotFoundError:
        task_data = {}
    return task_data

task = load_task()

def save_task(task_data):
    with open("task.json", "w") as file:
        json.dump(task_data, file)

def add_task(description):
    task[time.ctime()] = description
    save_task(task)

def delete_task(key):
    if key in task:
        del task[key]
        save_task(task)
        print("Замітка видалена")
    else:
        print("Немає такої замітки")

menu = input("Введіть номер опції (1 - список, 2 - додати, 3 - видалити): ")

while True:
    menu = input("Введіть номер опції (1 - список, 2 - додати, 3 - видалити, 4 - вийти): ")

    match menu:
        case "1":
            print("Список завдань:")
            for key, value in load_task().items():
                print(key, value)

        case "2":
            print("Введіть замітку:")
            description = input("Введіть опис завдання: ")
            add_task(description)

        case "3":
            print("Введіть дату таску для видалення:")
            key = input()
            delete_task(key)

        case "4":
            save_task(task)  # Зберігаємо завдання перед виходом
            print("Вихід з програми.")
            break  # Виходимо з циклу

        case _:
            print("Неправильний вибір. Будь ласка, введіть ще раз.")


