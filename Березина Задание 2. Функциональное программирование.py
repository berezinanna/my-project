def is_in_range(number):
    return 10 <= number <= 20
def main():
    number = int(input("Введите число для проверки диапазона (10-20): "))
    if is_in_range(number):
        print("Число находится в диапазоне от 10 до 20.")
    else:
        print("Число не находится в диапазоне от 10 до 20.")

if __name__ == "__main__":
    main()
def calculate_delivery_cost(item_count):
    if item_count == 0:
        return 0
    return 10.95 + (item_count - 1) * 2.95

# Пример вызова функции
def main():
    item_count = int(input("Введите количество товаров в заказе: "))
    total_cost = calculate_delivery_cost(item_count)
    print(f"Общая сумма доставки: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
import random

def generate_random_password():
    password = ''.join(str(random.randint(1, 10)) for _ in range(10))
    return password

# Пример вызова функции
def main():
    password = generate_random_password()
    print(f"Сгенерированный пароль: {password}")

if __name__ == "__main__":
    main()