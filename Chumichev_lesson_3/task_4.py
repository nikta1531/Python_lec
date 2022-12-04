# Напишите программу, которая будет
# преобразовывать десятичное число в двоичное.
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

b_number = []
number = int(input("Введите десятичное число: "))

while number > 0:
    b_number.append(number % 2)
    number //= 2

print(*b_number[::-1], sep='')