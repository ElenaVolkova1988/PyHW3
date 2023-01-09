# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
import random

my_list=[ ]
my_list2=[]
for _ in range ( 5 ):
    my_list.append(round(random.uniform(0,5),0))       # рандомное заполнение списка из 5 элементов
for i in range(len(my_list)):
    first=my_list[0]
    if i < len(my_list)/2 :
        last=len(my_list)-1
        product=first*last
        i+=1
        my_list2.append(product)
        
      
print(my_list)
print(my_list2)    
   int ProductNumber (int [] num)
{
   int product =0;
   int first= num[0];
   int last=num[num.Length-1];
   for(int i=0; i<num.Length/2; i++)
{
     product=first*last; 