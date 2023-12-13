import json
import time

def start_timer():
    start_time = time.time()
    print("Таймер запущено!")
    return start_time

def load_timer_state():
    try:
        with open('timer_state.json', 'r') as file:
            timer_state = json.load(file)
    except FileNotFoundError:
        timer_state = {"start_time": 0, "elapsed_time": 0}
    return timer_state


def save_timer_state(timer_state):
    with open('timer_state.json', 'w') as file:
        json.dump(timer_state, file)


#стан таймера
timer = load_timer_state()
start_time = timer["start_time"]
elapsed_time = timer["elapsed_time"]

# Якщо таймер був запущений, продовжити відлік
if start_time != 0:
    elapsed_time += time.time() - start_time

# Основний цикл програми
while True:
    print("\nМеню:")
    print("1. Запустити/перезапустити таймер")
    print("2. Вивести час виконання")
    print("3. Вийти з програми")

    choice = input("Виберіть опцію: ")

    if choice == "1":
        start_time = start_timer()
        timer["start_time"] = start_time
    elif choice == "2":
        current_elapsed_time = elapsed_time
        if start_time != 0:
            current_elapsed_time += time.time() - start_time
        print("Час виконання", current_elapsed_time)
    elif choice == "3":
        timer["elapsed_time"] = elapsed_time
        save_timer_state(timer)
        break
    else:
        print("Error")