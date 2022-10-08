'''
5. ** Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
in
"poly.txt"
"poly_2.txt"

out in the file
3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

in
"poly.txt"
"poly_2.txt"

out
The contents of the files do not match!
'''

def poly_list (first, second):
    with open(first, "r", encoding = "utf-8") as file_1, \
        open(second, "r", encoding = "utf-8") as file_2:
        first_file = file_1.readlines()
        second_file = file_2.readlines()

        if len(first_file) == len(second_file):
            with open("for_task_5.txt", "a", encoding = "utf-8") as result:
                for i,k in enumerate(first_file):
                    result.write(f"{k[:-5]} + {second_file[i]}")
        else: 
            print("The contents of the files do not match!")
poly_list("poly.txt", "poly_2.txt")