'''
2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
Простые делители числа

in -> 54
out -> [2, 3, 3, 3]

in -> 9990
out -> [2, 3, 3, 3, 5, 37]

in -> 650
out -> [2, 5, 5, 13]
'''

def multiplier (n):
    result = []
    for i in range(2, n+1):            
        if n % i == 0: 
            while n % i ==0:
                n /= i
                result.append(i)
        else: 
            continue
    return result


N = int(input("Введите натуральное число N: "))
print(multiplier(N))
