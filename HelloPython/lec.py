# s = 'hello world'
# a = 123
# b= 1.23
#
# print(s) # вывдо строки
# print(a, '-',b, '-', s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}') # интерполяция
#
# f = True
# print(f)

# list = ['1', '2' , '3']
# col = ['hello', 1, 2, 4.5, True]
# print(list)
# print(col)

# print('Введите а')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a, '+', b, '=', a+b)
# # print('{} {}'.format(a, b))
# # print(f'{a} {b}')

# Арифметические операции
# +, -, *, /, %, //, **
# (), Сокращенные операции
# a = 1.312
# b = 3
# c = round(a * b, 3)
# print(c)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, **
# is, is not, in, not in
# gen

# func = 1
# T = 4
# x = 2
# print(func<T>(x))

# f = [1,2,3,4]
# print(f)
# print(not 2 in f)
#
# is_odd = not f[0] % 2
# print(is_odd)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# for i in range(1, 10, 2):
#     print(i)

# text = 'съешь ещё этих мягких французских булок'
#
# # help(text.istitle)
# # print(len(text))        # 39
# # print('ещё' in text)    # True
# # print(text.isdigit())   # False
# # print(text.islower())   # True
# # print(text.replace('ещё', 'ЕЩЁ'))
#
# for c in text:
#     print(c)

# Списки: введение
# list = list
# numbers = [1, 2, 3, 4, 5]
# print(numbers)        # [1, 2, 3, 4, 5]
# ran = range(1, 6)
# numbers = list(ran)
# print(numbers)          # [1, 2, 3, 4, 5]
# numbers[0] = 10
# for i in numbers:
#     i *= 2
#     print(i)             # [20, 4, 6, 8, 10]
# print(numbers)           # [10, 2, 3, 4, 5]

# Функции
# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
#
# arg = 2.3
# print(f(arg))
# print(type(f(arg)))


# Семинар

# num1 = int(input("Enter num1 "))
# num2 = int(input("Enter num2 "))
#
# if num1**2 == num1 or num2**2 == num1:
#     print('Yes')
# else:
#     print('No')

# Примеры:
#
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# i = 0
# nums = []
# while i < 5:
#     nums.append(int(input()))
#     i += 1
# print(max(nums))

# max_number = float('-inf')
# for i in range(1, 6):
#     number = int(input(f'Введите число {i}: '))
#     if number > max_number:
#         max_number = number
# print(max_number)

# count = 1
# list_numbers = []
# for i in range(1, 6):
#     number = int(input(f'Введите число {i}: '))
#     list_numbers.append(number)
# print(list_numbers)
# print(max(list_numbers))


# a = int(input())
# for i in range(-a, a):
#     print(i, end=', ')
# print(a)

# n = float(input('введите число: '))
# if n % 1 == 0:
#     print('нет')
# else:
#     n1 = int(n % 1 * 10)
#     print(n1)

# n = float(input('введите число: '))
# if n != int(n):
#     print(int(n * 10 % 10))
# else:
#     print('Нет')