"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""
n = int(input('Введите количество элементов в прогрессии n: '))
a1 = int(input('Введите первый элемент прогрессии a1: '))
d = int(input('Введите разность прогрессии d: '))
min = int(input('Введите минимум диапазона min: '))
max = int(input('Введите максимум диапазона max: '))

i = 0
list1 = []
list1.append(a1)
for i in range(2,n + 1) :
    list1.append(a1 + (i - 1) * d)
list2 = []
for i in range(len(list1)) :
    if min <= list1[i] <= max :
        list2.append(i)
print(list2)
