# 39. Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
#
# Вывод:
# 3 3 2 12

# # через множества
# n = int(input('Введите количество элементов в первом списке: '))
# first_set = set()
# second_set = set()
# for _ in range(n):
#     number = int(input('Введите числа: '))
#     first_set.add(number)
#
# m = int(input('Введите количество элементов во втором списке: '))
# for _ in range(m):
#     number = int(input('Введите числа: '))
#     second_set.add(number)
#
# dif = first_set.difference(second_set)
# print(dif)
#
# # через списки
# n = int(input('Введите количество элементов в первом списке: '))
# first_list = []
# second_list = []
# for _ in range(n):
#     number = int(input('Введите числа: '))
#     first_list.append(number)
#
# m = int(input('Введите количество элементов во втором списке: '))
# for _ in range(m):
#     number = int(input('Введите числа: '))
#     second_list.append(number)
#
# for el in first_list:
#     if el not in second_list:
#         print(el, end=' ')

# 41. Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

# Ввод:
# 5
# 1 2 3 4 5
#
# Вывод:
# 0
#
# Ввод:
# 5
# 1 5 1 5 1
#
# Вывод:
# 2

# n = int(input('Введите количество элементов в списке: '))
# some_list = []
# count = 0
# for _ in range(n):
#     number = int(input('Введите числа: '))
#     some_list.append(number)
#
#
# for i in range(1, len(some_list) - 1):
#     if some_list[i] > some_list[i - 1] and some_list[i] > some_list[i + 1]:
#         count += 1
# print(some_list, count)

# 43. Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

# Ввод:
# 1 2 3 2 3 3
# Вывод:
# 2

# n = int(input('введите количесво символов в первом списке: '))
# list1 = []
# for _ in range (n):
#     list1.append(int(input('введите значение элемента первого списка: ')))
# a = set(list1)
# count_res = 0
# for i in a:
#     count = 0
#     for j in list1:
#         if i == j:
#             count += 1
#     count_res += count // 2
# print(count_res)
