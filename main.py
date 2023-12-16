# Завдання 1
# Створіть два окремих "мікросервіси" (дві окремі
# програми). Одна програма створює та експортує дані у
# форматі JSON, а інша програма завантажує та обробляє ці
# дані. Це може бути, наприклад, система, яка створює та
# обробляє замовлення.


import json


class OrderCreator:
    def create_order(self, order_id, product_name, quantity):
        order_data = {
            "order_id": order_id,
            "product_name": product_name,
            "quantity": quantity
        }
        return json.dumps(order_data)


if __name__ == "__main__":
    order_creator = OrderCreator()

    order_id = int(input("Введіть номер замовлення: "))
    product_name = input("Введіть назву продукту: ")
    quantity = int(input("Введіть кількість: "))

    order_data = order_creator.create_order(order_id, product_name, quantity)

    with open('order.json', 'w') as file:
        file.write(order_data)

    print("Замовлення створено та збережено у файл order.json.")

import json

class OrderProcessor:
    def process_order(self, order_json):
        order_data = json.loads(order_json)
        print("Обробка замовлення:")
        for key, value in order_data.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    with open('order.json', 'r') as file:
        loaded_order_json = file.read()

    order_processor = OrderProcessor()
    order_processor.process_order(loaded_order_json)
