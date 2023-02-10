number_of_tickets = int(input("Сколько билетов желаете приобрести? "))

total = 0

for i in range(number_of_tickets):
    age = int(input(f"Введите возраст {i + 1} посетителя: "))
    if age < 18:
        continue
    elif 18 <= age <= 25:
        total += 990
    else:
        total += 1390

discount_prise = int(total * 0.9)
if number_of_tickets > 3:
    print(f'Сумма к оплате с учётом скидки 10%: {discount_prise}', "руб.")
else:
    print(f'Сумма к оплате: {total}', "руб.")