class Order:
    TAX_RATE = 0.08  # 8% налог
    SERVICE_CHARGE = 0.05  # 5% сервисный сбор

    def __init__(self, customer):
        self.customer = customer
        self.dishes = []

    def add_dish(self, dish):
        if isinstance(dish, Dish):
            self.dishes.append(dish)
        else:
            raise ValueError("Можно добавлять только объекты класса Dish.")

    def calculate_total(self):
        return sum(dish.price for dish in self.dishes)

    def __str__(self):
        dish_list = "\n".join([str(dish) for dish in self.dishes])
        return f"Order for {self.customer.name}:\n{dish_list}\nTotal: ${self.calculate_total():.2f}"


class Dish:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Dish: {self.name}, Category: {self.category}, Price: ${self.price:.2f}"


class Customer:
    def __init__(self, name, membership="Regular"):
        self.name = name
        self.membership = membership
