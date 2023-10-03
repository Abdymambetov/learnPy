
# def min(arg: list) -> int:
#     c = 1
#     value = arg[0]
#     for i in arg:
#         print(f'круг {c}: {value} - {i}')
#         c+=1
#         if value <= i:
#             value = i
    
#     return value


# print(min([2, 5, 0.5, 7]))

# def plus(*args):
#     return sum(args), args

# print(plus(1,2,3,4,5,6,7,8,9))

# def menu(drink, eat):
#     return dict(drink=drink, eat =eat)

# print('monday:', menu('cola', 'pzza'))
# print('tuesday:', menu('water', 'hot-dog'))


# contacts = {
#     'police': '102',
#     'Alina': '0707',
#     'Meder': '0707270138'
# }

# def find_contact(name):
#     if name in contacts.keys():
#         return True
#     return False

# def new_contact(name, phone):
#     if find_contact(name):
#         return f'контакт {name} уже есть!'
#     else:
#         contacts[name] = phone
#         return f'контакт {name} добавлен, номер {phone}'

    
# def delete_contact(name):
#     if find_contact(name):
#         del contacts[name]
#         return f'контакт {name} удален!'
#     else: 
#         print(f'контакт не найден')
#         user_input = input('Введите сюда имя которое хотите удалить: ')
#         if user_input:
#             delete_contact(user_input)
    
# print(new_contact('Artem', '0555555'))
# print(delete_contact('Abd'))
# print(contacts)


# def arifMath(*args):
#     return sum(args) // len(args)

# print(arifMath(1,2,3,4,5,6,7,8,9))

####короткий вариант:
# plus = lambda *args: sum(args) // len(args)
# print(plus(1,2,3,4,5,6,7,8,9))


#######
# def evenOdd(num):
#     if isinstance(num, int):
#         return num % 2 == 0
#     else:
#         return None
    
# def exemple():
#     user_inp = int(input('Введите число: '))
#     if user_inp:
#         return evenOdd(user_inp)
# print(exemple())


# #####
# def check_spelling(sentence):
#     if sentence[0].isupper() and sentence.endswith('.'):
#         return sentence
#     else:
#         return "Предложение должно начинаться с заглавной буквы и заканчиваться точкой."
    
# #######
# def subsecNum(subsec, num):
#     closest = None
#     minimum_distance = None

#     for sub in subsec:
#         distance = abs(sub-num)
#         print(abs(sub - num), end='- ')
#         if minimum_distance is None or distance < minimum_distance:
#             minimum_distance = distance
#             closest = sub
#     return closest

# sub1 = [5, 20.18, 103, 4]
# num1 = 27
# print(subsecNum(sub1, num1))  # Вывод: 20.18

# sub2 = (312, 996, 31, 1991)
# num2 = 1000
# print(subsecNum(sub2, num2)) 

numbers = [6,2,67,34,91]
target = 100
minV = numbers[0]
for i in numbers:
    print(f'круг: {abs(target - i), {target - minV}}')
    if abs(target - i) < abs(target - minV):
        minV = i

changed = [abs(target - i) for i in numbers]
print(f'индекс {numbers[changed.index(min(changed))]}')
print(minV)
print(changed)



