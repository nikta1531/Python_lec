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

# print("x, y, z")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(x,y,z, '\t', not(x or y or z) == (not x and not y and not z))

###
###
# lst = []
#
#
# def add_to_lst(item):
#     if isinstance(item, int):
#         lst.append(item)
#
#
# add_to_lst(66)
# add_to_lst('ww')
# add_to_lst(65.5)
# add_to_lst(2)
# add_to_lst(None)
# print(lst)

##############################
'''1. Напишите программу, которая принимает на вход число N и выдаёт
    последовательность из N членов.

    *Пример:*

    - Для N = 5: 1, -3, 9, -27, 81
'''
# n = int(input())
# count = 1
# for i in range(n-1):
#     print(f'{count}', end=', ')
#     count = count * (-3)
# print(count)
#####################################
# N = 5
#
#
# def sequence(n):
#     for i in range(n):
#         print((-3) ** i, end=' ')
#
#
# sequence(N)
#####################################
# n = int(input())
# for i in range(1, n+1):
#     if i % 2:
#         print(3**(i-1), end=', ')
#     else:
#         print(-3**(i-1), end=', ')
'''
2. Для натурального n создать список, 
   состоящий из элементов последовательности 3n + 1.

    *Пример:*

    - Для n = 4: [1, 4, 7, 10, 13] 
'''
# n = int(input())
# array = []
# for i in range(n + 1):
#     array.append(3 * i + 1)
# print(array)
'''
3. Напишите программу, в которой пользователь будет
    задавать две строки, 
   а программа - определять количество вхождений
   одной строки в другой.

s1 = 'aa ab aba ewfwef'
s2 = 'aba'

print(s1.count(s2))
'''
# str1 = input("1: ")
# str2 = input("2: ")
#
# count = 0
#
# for i in range(len(str1) - (len(str2) - 1)):
#     if str2 == str1[i:i+len(str2)]:
#         count += 1
#
# print(f"Вторая строка входит в первую {count} раз(а).")
########################
# def something_input(in_type, wellcome_text):
#     input_str = input(f'{wellcome_text} : ')
#     if in_type == 'int':
#         result = int(input_str)
#     elif in_type == 'float':
#         result = float(input_str)
#     else:
#         result = input_str
#     return result
#
#
# def print_task_no(no):
#     print('\n')
#     print(f'task {no}')
#
# print_task_no(3)
# str1 = something_input('str', 'input number string 1')
# str2 = something_input('str', 'input number string 2')
# if len(str1) > len(str2):
#     str1, str2 = str2, str1
# length = len(str1)
# count = 0
# for i in range(len(str2) - length):
#     tmp = []
#     for j in range(length):
#         tmp.append(str2[j + i])
#         print(tmp)
#         print(''.join(tmp))
#     if str1 == ''.join(tmp):
#         count += 1
# print(count)

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close()
#
#
# exit()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
#
# exit()

# Числа Фибоначи
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
#
# list = []
# for i in range(1, 10):
#     list.append(fib(i))
# print(list) # 1 1 2 3 5 8 13 21 34


###########################################
###########################################
###########################################
# 5 Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint
# from  random import randint
#
#
# def mix(lst):
#     for i in range(len(lst)):
#         new_i = randint(0, len(lst) - 1)
#         lst[i], lst[new_i] = lst[new_i], lst[i]
#
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# mix(lst)
# print(lst)


# from time import time
#
# print(time())

# 1.
# Реализуйте алгоритм задания случайных
# чисел
# без
# использования
# встроенного
# генератора
# псевдослучайных
# чисел.

# from time import time
#
# def randomtime(max):
#     time1 = time()
#     time1 = (time1 - int(time1))
#     return int(time1 * max)
#
# print(randomtime(1000))

#
# 2.
# Задайте
# список.Напишите
# программу, которая
# определит, присутствует
# ли
# в
# заданном
# списке
# строк
# некое
# число.
# ['22', '33', '123', 'fwefe', 'ytyy', '55']
#
# f(n)

# lst = ['22', '33', '123', 'fwefe', 'ytyy', '55']
# u = 55
#
# print(lst)
#
# for i in lst:
#     if i.isdigit() and int(i) == u:
#         print('данное число есть в скиске')

# if nums in lst:
#     print(nums)

# result = 'нет'
# for i in lst:
#     if nums == i:
#         result = 'данное число есть в скиске'
#         break
# print(result)

# lst = ['22', '33', '123', 'fwefe', 'ytyy', '55']
#
# def f(l1, n):
#     for item in l1:
#         if item.isdigit() and int(item) == n:
#             return True
#         return False
#
# print(f(lst, 55))


#
# 3.
# Напишите
# программу, которая
# определит
# позицию
# второго
# вхождения
# строки
# в
# списке
# либо
# сообщит, что
# её
# нет.
#
# *Пример: *
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# def pro_list(lst_):
#     result = []
#     for i in range(len(lst_) // 2 + 1):
#         result.append(lst_[i] * lst_[- i - 1])
#     print(result)
#
# lst1 = [1,2,3,4,5]
# print(pro_list(lst1))

# def fib(n):
#     if n == 1:
#         return 0
#     elif n == 0:
#         return 1
#
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(10))


# mem = {1: 0, 2: 1}
#
#
# def fib(n):
#     if n not in mem:
#         mem[n] = fib(n - 1) + fib(n - 2)
#
#         return mem[n]
#
#
# print(fib(10))
# print(mem)


