# Сгенерировать файл из чисел в диапазоне [-2, 2], используя утилиту
# utils/gen_4_30.py. Написать программу, считывающую все значения чисел
# из сгенерированного файла
# и выводящую в stdout только уникальные значения.

#
with open("data_4_30_1.txt", "r") as fr:
    a = []
    for i in fr:
        x, y = i.rstrip().split(" ")
        # print(i)
        a.append(x)
        a.append(y)
    print(a)
    print(set(a))



