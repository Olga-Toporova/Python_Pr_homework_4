'''
4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
in
9
5
3

out in the file
3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
4*x^2 - 4 = 0

in
0
-1
4

out in the file
3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
4*x^2 - 4 = 0
2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0
'''
import random
from random import choice


def write_file(str):
    with open('for_task_4.txt', 'a') as file:
        file.write(f'{str} \n')

def create_str(list_in):
    new_list = list_in[::-1]
    write = ''
    length = len(new_list)
    if length == 1:
        write = 'x = 0'
    else:
        for i in range(length):
            if i != new_list[i] == 0: write += f"{choice('+-')} "
            elif i != length - 1 and new_list[i] != 0 and i != length - 2:
                write += f'{new_list[i]}x^{length-i-1} '
                if new_list[i+1] != 0 and new_list[i] > 0: write += f"{choice('+-')} "
            elif i == length - 2 and new_list[i] != 0:
                write += f'{new_list[i]}x '
                if new_list[i+1] != 0 and new_list[i] > 0: write += f"{choice('+-')} "
            elif i == length - 1 and new_list[i] != 0: write += f'{new_list[i]} = 0 '
            elif i == length - 1 and new_list[i] == 0: write += ' = 0 '
    return write

for _ in range(3):
    k = int(input("Введите натуральную степень k = "))
    koef = [random.randint(0,10) for i in range(k)]
    write_file(create_str(koef))
