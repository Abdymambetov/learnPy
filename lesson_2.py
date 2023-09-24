time = input('What timeis it now?')

if time == 'morning':
    print('Good morning!')
elif time == 'evening':
    print('Good evening!')
elif time == 'day':
    print('Good day!')
else: 
    print('Greeatings!')


print('abc' is 'abs')
####

color = input('What traffic light?')
if color == 'red':
    print('stop')
elif color == 'yellow':
    print('wait')
elif color == 'green':
    print('go')
else: 
    situation = input('What do yout see?')
    if situation == 'ГАИ':
        print('Слушай гаишника')
    elif situation == 'преграда':
        print('обойди преграду')
    else:
        print('Стой на месте')

###
date_input = input('Введите свою дату рождения и месяц')

date_parts = date_input.split(',')

if len(date_parts) !=2:
    date_parts = date_input.split('.')
if len(date_parts) !=2:
    date_parts = date_input.split('/')

if len(date_parts) != 2:
    print('Неверный формат даты')
else: 
    day, month = map(int, date_parts)

    day_str = str(day).zfill(2)
    month_str = str(month).zfill(2)

    if (month == 3 and 21 <= day <= 31) or (month == 4 and 1 <= day <= 19):
        zodiac_sign = "Овен"
    elif (month == 4 and 20 <= day <= 30) or (month == 5 and 1 <= day <= 20):
        zodiac_sign = "Телец"
    elif (month == 5 and 21 <= day <= 31) or (month == 6 and 1 <= day <= 20):
        zodiac_sign = "Близнецы"
    elif (month == 6 and 21 <= day <= 30) or (month == 7 and 1 <= day <= 22):
        zodiac_sign = "Рак"
    elif (month == 7 and 23 <= day <= 31) or (month == 8 and 1 <= day <= 22):
        zodiac_sign = "Лев"
    elif (month == 8 and 23 <= day <= 31) or (month == 9 and 1 <= day <= 22):
        zodiac_sign = "Дева"
    elif (month == 9 and 23 <= day <= 30) or (month == 10 and 1 <= day <= 22):
        zodiac_sign = "Весы"
    elif (month == 10 and 23 <= day <= 31) or (month == 11 and 1 <= day <= 21):
        zodiac_sign = "Скорпион"
    elif (month == 11 and 22 <= day <= 30) or (month == 12 and 1 <= day <= 21):
        zodiac_sign = "Стрелец"
    elif (month == 12 and 22 <= day <= 31) or (month == 1 and 1 <= day <= 19):
        zodiac_sign = "Козерог"
    elif (month == 1 and 20 <= day <= 31) or (month == 2 and 1 <= day <= 18):
        zodiac_sign = "Водолей"
    else:
        zodiac_sign = "Рыбы"

print(f'Ваш знак зодиака: {zodiac_sign}\nВаш день рождение; {day_str}.{month_str}')

####

date_input = input("Введите дату рождения (дд.мм, дд/мм, дд,мм): ")


for separator in [',', '.', '/']:
    if separator in date_input:
        day, month = map(int, date_input.split(separator))
        break
    else:
        print("Неверный формат ввода даты.")
else:
    signs = ["Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец", "Козерог", "Водолей", "Рыбы"]
    days_in_month = [0, 20, 19, 21, 20, 21, 22, 23, 23, 23, 22, 22]
    zodiac_sign = signs[month - (day < days_in_month[month])]
    print(f"Ваш знак зодиака: {zodiac_sign}, Дата рождения: {day:02d}.{month:02d}")