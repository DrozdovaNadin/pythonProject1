# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
#
# 6 -> да
# 7 -> да
# 1 -> нет

y = int(input("Введите день недели: "))
if y == 6 or y == 7:
    print('да, выходной')
else:
    print("нет, рабочий день")