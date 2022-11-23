# Напишите программу, которая принимает на вход координаты
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

point_x = int(input("Введите точку X: "))
point_y = int(input("Введите точку Y: "))

if point_x > 0 and point_y > 0:
    print(f'x={point_x}; y={point_y} -> 1')
elif point_x < 0 and point_y > 0:
    print(f'x={point_x}; y={point_y} -> 2')
elif point_x < 0 and point_y < 0:
    print(f'x={point_x}; y={point_y} -> 3')
elif point_x > 0 and point_y < 0:
    print(f'x={point_x}; y={point_y} -> 4')
else:
    print("Не выполнены условия X ≠ 0 и Y ≠ 0")