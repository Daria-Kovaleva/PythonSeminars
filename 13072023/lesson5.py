# 31. Последовательностью Фибоначчи называется последовательность чисел
# a0, a1, ..., an, ..., где:
# a0 = 0,
# a1 = 1,
# ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# Input: 7
# Output: 13

# n = int(input('Введите число: '))
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fib(n - 2) + fib(n - 1)
#
# print(fib(7))
#
# def fib_while(n):
#     if n == 1 or n == 2:
#         return 1
#     first = 1
#     second = 1
#     temp = first + second
#     count = 3
#     while count < n:
#         first = second
#         second = temp
#         temp = first + second
#         count += 1
#     return temp
#
# print(fib_while(7))

# import time
#
# start = time.perf_counter()
# print(fib(30))
# end = time.perf_counter()
# duration = end - start
#
# start = time.perf_counter()
# print(fib_while(30))
# end = time.perf_counter()
# duration2 = end - start
#
# print(duration / duration2)

# 33. Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

# Input: 5 -> 4 8 9 1 2
# Output: 4 8 1 1 2

# n = int(input('Введите кол-во оценок: '))
# some_list = []
# for _ in range(n):
#     number = int(input('Введите числа: '))
#     some_list.append(number)
# maxx = max(some_list)
# minn = min(some_list)
# for ind in range(0, n):
#     if some_list[ind] == maxx:
#         some_list[ind] = minn
#
# print(some_list)

# 35. Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
#
# Input: 5
# Output: yes

# n = int(input('Введите число: '))
# def a(x):
#     for div in range(2, int(n ** 0.5) + 1):
#         if n % div == 0:
#             return 'no'
#     return 'yes'
#
# print(a(n))

# 37. Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
#
# Input: 2 -> 3 4
# Output: 4 3

# def change(n):
#     if n == 0:
#         return ''
#     num = int(input('Введите числа: '))
#     return change(n-1)+f' {num}'
#
# n= int(input('Введите число: '))
print(change(n))
