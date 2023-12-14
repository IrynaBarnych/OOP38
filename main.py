# Завдання 3
# До вже реалізованого класу «Дріб» додайте можливість стиснення та розпакування даних з
# використанням json та pickle.

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

watch1 = Watch("Чип", "Швейцарія", 2020, 200, "Ручний")
watch2 = Watch("Дейл", "Китай", 2022, 300, "Настінний")

# Годинник 1
print(f"Модель: {watch1.get_model()}")
print(f"Виробник: {watch1.get_manufacturer()}")
print(f"Рік випуску: {watch1.get_year()}")
print(f"Цена: {watch1.get_price()}")
print(f"Вид годинника: {watch1.get_watch_type()}")

# Годинник 2
print(f"Модель: {watch2.get_model()}")
print(f"Виробник: {watch2.get_manufacturer()}")
print(f"Рік випуску: {watch2.get_year()}")
print(f"Цена: {watch2.get_price()}")
print(f"Вид годинника: {watch2.get_watch_type()}")

price_difference = watch1 - watch2
print(f"Різниця в ціні: {price_difference} євро")

if watch1.is_same_watch_type(watch2):
    print("У годинників однаковий тип.")
else:
    print("У годинників різний тип.")