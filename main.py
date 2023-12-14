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
            task = json.load(file)
    except FileNotFoundError:
        task = {}
    return task

task = load_task()

def save_task(task):
    with open("task.json", "w") as file:
        json.dump(task, file)

def add_task(description):
    task[time.ctime()] = description
    save_task(task)

def delete_task(key):
    if key in task:
        del task[key]
        save_task(task)
        print("замітка видалена")
    else:
        print("Немає такої замітки")

menu = input()
match menu:
    case "1":
        print("список завдань")
        for key, value in load_task().items():
            print(key, value)

    case "2":
        print("Введіть замітку")
        description = input("Введіть опис завдання")
        add_task(description)
    case "3":
        print("Введіть дату таску для видалення: ")
        key = input()
        #key = task.keys()[0]
        delete_task(key)