# Завдання 3
# До вже реалізованого класу «Стадіон» додайте можливість
# стиснення та розпакування даних з використанням json та
# pickle.

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