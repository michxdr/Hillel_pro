class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def change_price(self, new_price):
        self.price = new_price

    def change_quantity(self, amount):
        self.quantity += amount
        if self.quantity < 0:
            self.quantity = 0


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.order_list = []

    def add_new_order(self, order):
        self.order_list.append(order)


class Order:
    def __init__(self, product_list=None):
        self.product_list = product_list if product_list else []

    def add_product(self, product, quantity=1):
        """Додає товар із вказаною кількістю"""
        self.product_list.append({'product': product, 'quantity': quantity})

    def sum_of_order(self):
        total = 0
        for item in self.product_list:
            total += item['product'].price * item['quantity']
        return total

    def show_order(self):
        """Показує деталі замовлення"""
        print("\nЗАМОВЛЕННЯ:")
        print("-" * 50)
        for item in self.product_list:
            product = item['product']
            quantity = item['quantity']
            subtotal = product.price * quantity
            print(f"{product.name} x{quantity} = {subtotal} грн")
        print("-" * 50)
        print(f"ВСЬОГО: {self.sum_of_order()} грн")


class Shop:
    def __init__(self):
        self.products = []
        self.customers = []

    def load_products(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines[1:]:
                    line = line.strip()
                    if line:
                        name, category, price, quantity = line.split('|')
                        product = Product(name, category, float(price), int(quantity))
                        self.products.append(product)
            print(f"Завантажено {len(self.products)} товарів")
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено!")
        except Exception as e:
            print(f"Помилка: {e}")

    def load_customers(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines[1:]:
                    line = line.strip()
                    if line:
                        name, email = line.split('|')
                        customer = Customer(name, email)
                        self.customers.append(customer)
            print(f"Завантажено {len(self.customers)} клієнтів")
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено!")
        except Exception as e:
            print(f"Помилка: {e}")

    def show_products(self):
        print("\nТОВАРИ В МАГАЗИНІ:")
        print("-" * 70)
        for i, product in enumerate(self.products, 1):
            print(f"{i}. {product.name} ({product.category}) - "
                  f"{product.price} грн, залишок: {product.quantity} шт")

    def show_customers(self):
        print("\nКЛІЄНТИ:")
        print("-" * 50)
        for i, customer in enumerate(self.customers, 1):
            print(f"{i}. {customer.name} ({customer.email}) - "
                  f"Замовлень: {len(customer.order_list)}")

    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def find_customer(self, name):
        for customer in self.customers:
            if customer.name.lower() == name.lower():
                return customer
        return None


# ПРИКЛАД ВИКОРИСТАННЯ
if __name__ == "__main__":
    # Створюємо магазин
    shop = Shop()

    shop.load_products('products.txt')
    shop.load_customers('customers.txt')

    shop.show_products()
    shop.show_customers()

    # Створюємо замовлення для клієнта
    print("\n" + "=" * 70)
    print("ПРИКЛАД СТВОРЕННЯ ЗАМОВЛЕННЯ")
    print("=" * 70)

    customer = shop.find_customer("Олена")
    if customer:
        # Створюємо замовлення
        order = Order()

        # Додаємо товари
        toy = shop.find_product("Ведмедик")
        lego = shop.find_product("LEGO Castle")

        if toy:
            order.add_product(toy, quantity=2)
        if lego:
            order.add_product(lego, quantity=1)

        order.show_order()

        customer.add_new_order(order)
        print(f"\nЗамовлення додано для {customer.name}")