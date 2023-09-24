
var = 'Meder'
should = 'M'
print(f'Hello {var} {should}' )

const = input("what's your name?")
name = const + ' Lox'
print(name)

a = int(str(5))
c=int(str(3))
b = a+c
print(type(b))
print(4/2)
print(6//3)
print(2**3)
print( 8%3)
print(round(45.81631745, 1))

age = int(input('Your age?'))
height = float(input('Your height?'))

print(f'Your height {height + 0.02} and you live in the word {2023-age}')

temp_1 = int(input('Введите погоду в Бишкеке: '))
temp_2 = int(input('Введите погоду в ИК: '))
temp_3 = int(input('Введите погоду в Нарыне: '))
temp_4 = int(input('Введите погоду в Таласе: '))
temp_5 = int(input('Введите погоду в Джалал-Абаде: '))
temp_6 = int(input('Введите погоду в Оше: '))
temp_7 = int(input('Введите погоду в Баткене: '))

sum = temp_1 + temp_2 + temp_3 + \
                + temp_4 + temp_5 + temp_6 +\
                + temp_7
average_sum = sum /7

print(sum)
print(f'{round(average_sum, 1)}C')