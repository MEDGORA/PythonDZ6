"""
Задача 30: Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""
n = int(input('Введите количество элементов в прогрессии n: '))
a1 = int(input('Введите первый элемент прогрессии a1: '))
d = int(input('Введите разность прогрессии d: '))
i = 0
list1 = []
list1.append(a1)
for i in range(2,n + 1) :
    list1.append(a1 + (i - 1) * d)
print(list1)