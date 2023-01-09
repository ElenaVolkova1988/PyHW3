# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

my_list=[ ]
my_list2=[]
for _ in range (5):
    my_list.append(round(random.uniform(0,5),2)) # рандомное заполнение списка из 5 элементов
for i in range(len(my_list)):     
    whole= int(my_list[i])                       #  отделение целой части от дробной 
    fractional= my_list[i]-int(my_list[i])
    print (my_list)
    print(f'Целая часть {whole} -> Дробная чать {fractional}')
    my_list2.append(fractional)                    # заполнила новый список только дробной частью
print(my_list2)
max=0
min=99999
for i in my_list2:                              # нахождение мин и макс
    if i>max:
        max=i
    if i<min:
        min=i
res=max-min
print(f'Максимальное дробное значение -> {max}, Минимальное дробное значение -> {min}, Разница между значениями -> {res}')