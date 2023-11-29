# Запрос количества билетов
num_tickets = int(input("Введите количество билетов: "))

# Инициализация переменных для подсчета стоимости и количества билетов скидки
total_cost = 0
discount_tickets = 0

# Цикл для каждого билета
for i in range(num_tickets):
    age = int(input(f"Введите возраст посетителя {i+1}: "))

    # Подсчет стоимости в зависимости от возраста
    if age < 18:
        total_cost += 0
    elif age >= 18 and age < 25:
        total_cost += 990
    else:
        total_cost += 1390

    # Проверка на количество билетов скидки
    if num_tickets > 3:
        discount_tickets = num_tickets

# Подсчет скидки и вывод итоговой суммы к оплате
if discount_tickets > 3:
    total_cost -= total_cost * 0.1

print(f"Сумма к оплате: {total_cost} руб.")

