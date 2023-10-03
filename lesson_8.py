#работа с файлами
from time import sleep
from random import randint, choice

file = open('exemple.txt', 'w', encoding='UTF-8')
file.write('Hello Meder')
file.close()

with open('exemple.txt', 'r', encoding='UTF-8') as file:
    for i in file.readlines():
        sleep(1)
        print(i, end='')
    print(file.read())
    print(file.readline())
    print(file.readlines()[:-1])


for i in range(1,10):
    for j in range(1,10):
        user = int(input(f'сколько будет {i} * {j}='))
        if user == i*j:
            print('correct')
        else:
            print(f'bad ({i*j})')



students = [1,5,6,7,8,3,2,9,11]
level = int (input("Выберите уровень: \n 1) easy \n 2) medium In 3) hard "))

with open('file.txt', 'w', encoding='UTF-8') as message:
    message.write(f'Участников: {len(students)}\n Уровень: {level}')


attempts = int(input('Сколько жизней вы хотите '))
if attempts <=0:
    print('Числа не меньше нуля')
    attempts = int(input('сколько жизней вы хотите? '))


right_answer = 0
wrong_answer = 0
while attempts !=0:
    if level == 1:
        until = 10
        first = randint(1, until)
        second = randint (1, until)
    if level == 2:
        until = 50
        first = randint(10, until)
        second = randint (10, until)
    if level == 3:
        until = 100
        first = randint(50, until)
        second = randint(50, until)

    chosen = choice(students)
    correct = first * second
    name = input(f'имя участника: {chosen} ').title()
    user_answer = int(input(f'Отвечает {name}\nСколько будет {first} * {second} = '))
    if user_answer == correct:
        with open('file.txt', 'a') as message:
            message.write(f'\n{name} {first} * {second} = {user_answer} '
                            f' ({correct}) правильно')
        right_answer +=1
        print('right')
    elif user_answer != correct:
        with open('file.txt', 'a') as message:
            message.write(f'\n{name} {first} * {second} = {user_answer} '
                            f' ({correct}) неправильно')
        wrong_answer+=1
        print('wrong')
    attempts -= 1
    students.remove(chosen)
    if wrong_answer == 3:
        print('У вас уже 3 ошибки, вы вылетаете из игры')
        break
    if attempts == 0:
        print(f'Попытки закончилиcь\nВаши ответы: правильные: {right_answer}, неправильные: {wrong_answer}')


winners = []
losers = []
with open('file.txt', 'r') as message:
    for i in message.readlines()[2:]:
        if i.split()[-1] == 'правильно':
            winners.append(i.split()[0])
            # print(i)
        else:
            losers.append(i.split()[0])

print(winners)
print(losers)
