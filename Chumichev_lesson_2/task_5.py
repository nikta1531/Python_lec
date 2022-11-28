# 5 Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint
from  random import randint


def mix(lst):
    for i in range(len(lst)):
        new_i = randint(0, len(lst) - 1)
        lst[i], lst[new_i] = lst[new_i], lst[i]


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mix(lst)
print(lst)