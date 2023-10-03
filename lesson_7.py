from random import choice

# assert 2!=1+1, 'так не пойдет'
if 2 != 1+1:
    raise Exception('не туда свернул братишка')

# words = ['python', 'javaScript', 'backend']
# new = ['frontend', 'android', 'manager']
# def upWord(word: str):
#     return word.title()


# def all_up(word: str):
#     return word.upper()

# def showWords(lst: list, func):
#     for i in lst:
#         print(func(i))

# showWords(words, upWord)
# showWords(words, lambda word: word.title())
# showWords(new, all_up)
# showWords(new, lambda word: word.upper())


# numbers = list(range(1,11))
# filtered = list(filter(lambda x: x%2 ==0, numbers))
# # filt = [i for i in numbers if i%2 !=0]

# mapped = tuple(map(lambda x: x**2, filtered))
# # maap = tuple([i**2 for i in filtered])
# print(numbers)
# print(filtered)
# # print(filt)
# print(mapped)
# print(maap)

# words = ['dddd', 'bb', 'ecc', 'a']

# new = sorted(words, key=lambda x: len(x))
# print(new)

# stId = [1,2,3,4,5,6,7,8,9,10]
# students = {}
# c = 0

# while c !=3:
#     asked = choice(stId)
#     try: 
#         name_user = input(f"Student's name under number: {asked} ")
#         rating = int(input(f'Enter rate for {name_user}: '))
#         students[name_user] = rating
#         stId.remove(asked)
#         c+=1
#     except:
#         print('вы вели не то значение')

# for k, v in students.items():
#     print(f'{k}: {v}')


def subNum(sub, num):
    closest = None
    minimum_distance = None

    for item in sub:
        distance = abs(item - num)
        if minimum_distance is None or minimum_distance > distance:
            minimum_distance = distance
            closest = item
    sortList = sorted(sub, key=lambda x: abs(x-num))

    return (closest, sortList)


# numbers = [312, 996, 31, 1991]
numbers = [5, 20.18, 103, 4]
number = 27
result = subNum(numbers, number)
print(result)  # Вывод: (996, [996, 312, 1991, 31]) 


def get_element(iterable):
    while True:
        try:
            user_input = input("Введите индекс элемента (или 'q' для выхода): ")
            if user_input.lower() == 'q':
                break
            index = int(user_input)
            if 0 <= index < len(iterable):
                print("Элемент по указанному индексу:", iterable[index])
            else:
                print("Неверный индекс. Допустимые индексы от 0 до", len(iterable) - 1)
        except ValueError:
            print("Ошибка: Введите целое число в качестве индекса.")
        except Exception as e:
            print("Произошла ошибка:", e)
            break

my_list = [1, 2, 3, 4, 5]
get_element(my_list)



