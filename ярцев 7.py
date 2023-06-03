import time

def express_delivery(items):
    cost = 10.95 + max(0, items-1)*2.95
    return cost

def delivery_decorator(func):
    def wrapper(items):
        start_time = time.time()
        result = func(items)
        end_time = time.time()
        print(f"Функция {func.__name__} была вызвана в {time.strftime('%H:%M:%S', time.localtime(start_time))} чтобы доставить {items} товаров стоимостью ${result:.2f}.")
        print(f"Время выполнения: {end_time - start_time:.4f} секунд.")
        return result
    return wrapper

express_delivery = delivery_decorator(express_delivery)

num_items = int(input("Введите количество элементов: "))
total_cost = express_delivery(num_items)
print(f"Общая стоимость экспресс-доставки составляет ${total_cost:.2f}.")