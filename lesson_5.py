# словари - dict, множества - set
# student = {
#     'name': 'Meder',
#     'age': 18,
#     25: True,
#     4.87: True,
#     (1,2,3): True,
#     False: True,
#     'height': 1.80,
#     'married': False,
#     'hobby': ['basketball', 'footlball', 'box', 'programing'],
#     'parents': (6541, 5041),
#     'rates': {
#         1: 'отично',
#         2: 'хорошо',
#         3: 'удов'
#     }
# }
# # new_student = dict(name='lina', age=19)
# # print(new_student)

# # добавление 
# student['name'] = 'Artem'
# student['hobby'].append('taiBoxing')
# # изменение
# student['married'] = True

# # удаление
# del student['age']
# parents = student.pop('parents')

# new_student = student
# print(new_student == student)
# print(new_student is student)

# student['rates'][3] = 'yjhvfkmyj'

# student['hobby'] = tuple(student['hobby'])


# # for i in student:
# #     print(f'{i} ==> {student[i]}')

# for key, value in student.items():
#     print(f'{key} - {value}')

# print(student.items())
# print(student.get('ten', 'вы ошиблись'))
# print(parents)
# print(student)

# set1 = {1,1,1,11,2,3,4,5,5,5,5,5,5,5,6}
# print(set1)

# while True:
#     user_inp = int(input('Number '))
#     if user_inp in set1:
#         set1.remove(user_inp)
#         print(set1)
#         break
#     else:
#         set1.add(user_inp)
#         print(set1)
#         break
# ceaser = {'курица', 'сыр', 'помидор'}
# pizza = {'сыр', 'колбаса', 'фета'}

# #difference - ищет разницу, можно заменить на -
# print(ceaser.difference(pizza))
# print(ceaser - pizza)

# #union - объединяет, можно заменить на символ |
# print(ceaser.union(pizza))
# print(ceaser | pizza)

# #intersection - ищет что есть и у обох, можно заменить на &
# print(ceaser.intersection(pizza))
# print(ceaser & pizza)

# # symmetric_difference - выведет все что есть в других, можно заменить на ^
# print(ceaser.symmetric_difference(pizza))
# print(ceaser ^ pizza)


data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510",
        "Fonex", "0543")

designations = []
codes = []

for item in data:
    if item.isdigit():
        codes.append(item)
    else: 
        designations.append(item)
print(designations)
print(codes)

operators = {}
index = 0

while index != len(codes):
    operators[designations[index]] = {codes[index]}
    index +=1

del operators['Katel']
del operators['Fonex']

operators['O!'].update({'0707', '0700'})
operators['Megacom'].update({'0555', '0990'})
operators['Beeline'].update({'0777', '0222'})
print(operators)

for key, value in operators.items():
    print(f'{key}: {value}')


# while index <len(operators):
#     operator_name = designations[index]
#     operator_code = codes[index]

#     if operator_name not in operators:
#         operators[operator_name] = set()
    
#     operators[operator_name].add(operator_code)

#     index +=1

# operators.pop('Fonex', None)
# operators.pop('Katel', None)

# operators.setdefault('O!', set()).add('0700')
# operators.setdefault('Megacom', set()).add('0700')
# operators.setdefault('Beeline', set()).add('0550')

# for key, value in operators.items():
#     print(key, value)
# print(operators)



country_flags = {
    "kg": {"red", "yellow"},     # Кыргызстан
    "ru": {"white", "blue", "red"},  # Россия
    "kz": {"blue", "yellow"},   # Казахстан
    "us": {"red", "white", "blue"},  # США
    "tr": {"red", "white"},     # Турция
}

while True:
    input_user = input('Введите цвет флага через запятые: ').split('-')
    matching_countries = [] 

    for country, flag_colors in country_flags.items():
        if all(color in flag_colors for color in input_user):
            matching_countries.append(country)

    if matching_countries:
         print("Домены стран с введенными цветами:", ", ".join(matching_countries))
    else:
        print("Нет стран с такими цветами в флаге.")

  
    again = input("Хотите продолжить? (да/нет): ")
    if again.lower() != 'да':
        break

