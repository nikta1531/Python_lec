# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности


lst = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
print(lst)
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)