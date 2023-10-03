# from sys import getsizeof as ges
# objects = ['python', 10, True, 6.3]
# nums= ['meder', 0, 12, 'javaScript']
# objects.append(False)


# objects.insert(2, 'meder')
# objects.extend(nums)
# print(objects)

# numbers = (True, 1,2,3,4,5, False)
# print(type(numbers))

# lst = [i for i in range(1,100)]
# tpl = tuple(i for i in range (1,100))

# print(ges(lst))
# print(ges(tpl))

data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for item in data_tuple:
    if isinstance(item, str):
        letters.append(item)
    else:
        numbers.append(item)

numbers.remove(6.13)
letters.append('Т')
numbers.insert(2, 2)

numbers.sort()
letters.reverse()
letters[1] = 'G'
letters[7] = 'c'

numbers = [x**2 for x in numbers]

letters = tuple(letters)
numbers = tuple(numbers)

print("кортеж letters:", letters)
print("кортеж numbers:", numbers)
