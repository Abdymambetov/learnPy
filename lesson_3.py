# word = 'python'

# for i in word: 
#     if i == 't':
#         continue
#     print(i.upper())
# for i in range(1,11):
#     if i == 3:
#         continue
#     print(i)

# odds = ''
# even = ''

# for i in range(1,6):
#     if i%2 ==0:
#         even += str(i)
#     else:
#         odds += str(i)

# print(odds)
# print(even)

# for i in range(1,4):
#     for k in range(1,4):
#         for j in range(1,4):
#             print(i, k, j)

# cash = 10000
# years = 5
# parcents = 0.05

# for i in range(1, years+1):
#     cash += cash * parcents
#     print(f'{i} год: {round(cash, 1)}')

# bol = True

# while bol == True: 
#     time = input('What timeis it now?')

#     if time == 'morning':
#         print('Good morning!')
#         bol = False
#     elif time == 'evening':
#         print('Good evening!')
#         bol=False
#     elif time == 'day':
#         print('Good day!')
#         bol=False
#     elif time == 'выход':
#         print('программа завершена!')
#         break
#     else: 
#         print('Greeatings!')
#         bol=True

# eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,. "
# rus = 'йцукенгшщзхъфывапролджэячсмитьбю '

# while True:
#     input_user = input('\nВведите слово ')
#     for i in input_user:
#         if i in eng:
#             print(rus[eng.index(i)], end='')
#         else:
#             print(eng[rus.index(i)], end='')


vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZбвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"

while True:
    input_text = input('Введите текст (для завершения введите "стоп"): ')

    if input_text.lower() == 'стоп':
        break  # Выход из цикла, если введено "стоп"

    vowel_count = 0
    consonant_count = 0
    text_length = 0

    # Убираем пробелы и знаки пунктуации из текста
    input_text = ''.join(filter(str.isalpha, input_text))

    for char in input_text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        text_length += 1

    vowel_percentage = (vowel_count / text_length) * 100
    consonant_percentage = (consonant_count / text_length) * 100

    print(f"Гласных букв: {vowel_count}")
    print(f"Согласных букв: {consonant_count}")
    print(f"Длина текста: {text_length} символов")
    print(f"Процент гласных: {vowel_percentage:.1f}%")
    print(f"Процент согласных: {consonant_percentage:.1f}%")
