# 2 Напишите программу, которая принимает
# на вход число N и выдает набор произведений чисел от 1 до N.
#
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# Запрещено использовать функцию factorial из библиотеки math.

nums = int(input('Введите число N: '))

n = 1
for i in range(nums):
    i = i + 1
    n = i * n

print(n, end=' ')