# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

number=int(input("Введите число:"))
my_list=[]
f1=1                           # Добавили переменные, от которых считать для положительных
f2=1
my_list.append(f1)             # в список добавляем ф1 
for i in range(2,number):      # цикл начинае со всторого, потому что первые два уже известны
    f1,f2=f2,f1+f2              # ф1 меняем на ф2, а ф2 на ф1+ф2
    my_list.append(f2)           # добавляем в список каждый раз только новую ф2 
f1=0                           # Добавили переменные, от которых считать для положительных
f2=1  
my_list.insert(0,f1)                       
for i in range(0,number):       
    f1,f2=f2,f1-f2 
    my_list.insert(0,f2)                                    
print (my_list)         
  