#for i in 1, 2, 3, 4: # i данная переменная будет существовать только в пределах данного цикла
 #   print("Ok")      # команда повториться столько раз сколько у нас переменных
from os import remove

# list_ = ['one', 'two', 'three']
# list_2 = [1, 3, 6, 7]
# sum_ = 0
# for i in range(len(list_2)): # функция range() возвращает нам последовательность чисел от 0 до того что мы укажем в скобках
#     sum_ += list_2[i]
#     print(sum_)

# for i in range(1, 11, 2): #start, stop, step числа выводятся от и до с шагом (напр 2)
#     print(i)
for i in range(1, 11):
    for j in range(1,11):
        print(f'{i} x {j} = {i+j}')