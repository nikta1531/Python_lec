# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarters = int(input("Введите номер четверти координат(1-4): "))

if quarters == 1:
    print("Первая ось: x > 0, y > 0")
elif quarters == 2:
    print("Вторая ось: x < 0, y > 0")
elif quarters == 3:
    print("Третья ось: x < 0, y < 0")
elif quarters == 4:
    print("Четвертая ось: x > 0, y < 0")
else:
    print('На координатной плоскости только 4 четверти')