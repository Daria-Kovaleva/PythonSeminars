# sl = 'a c b r t y'
# sl1 = sl.split()
# print(type(sl), type(sl1))
# print(sl)
# print(sl1)

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# Русские буквы оцениваются так:
#
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.

# k = 'ноутбук'

# summ = 0
# for i in k.upper():
#     summ += dict[1]
# print(summ)

# 25. Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# lst1 = 'a a a b c a a d c d d'.split()
# dict1 = {}
#
# for i in lst1:
#     if i in dict1:
#         print(f'{i}_{dict1[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     dict1[i] = dict1.get(i, 0) + 1