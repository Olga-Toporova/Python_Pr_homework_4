'''
3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

in -> 7
out ->
[4, 5, 3, 3, 4, 1, 2]
[5, 1, 2]

in -> -1

out ->
Negative value of the number of numbers!
[]

in -> 10

out ->
[4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
[6, 2, 3, 0, 9]
'''

def filter_unique_numbers(some_list):
    return [i for i in some_list if some_list.count(i)==1]

num_list = list(map(int, input("Введите значения через пробел: ").split()))
print(num_list)
print(filter_unique_numbers(num_list))
