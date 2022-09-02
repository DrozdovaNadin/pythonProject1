# Создать список, состоящий из кубов нечётных чисел от 1 до 1000
# (куб X - третья степень числа X):
#
# a) Вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.

number = 1
dir = []
n = 1000
a = 0
while number < n:
    if number % 2 != 0:
        number_1 = number**3
        dir.append(number_1)
        res = 0
        while number_1 > 0:
            got = number_1 % 10
            res = res + got
            number_1 //= 10
        if res % 7 == 0:
            a = a + number
    # print(number,'**3 =', number ** 3, '[', res, ']', 'накоп сумма', a)
    number += 1
print(dir)
print('Накопленная сумма', a)

dir1 = []
a1 = 0
for i in dir:
    i = i + 17
    res = 0
    dir1.append(i)
    while i > 0:
        got = i % 10
        res = res + got
        i //= 10
    if res % 7 == 0:
        a1 = a1 + number
print(dir1)
print('Накопленная сумма', a1)
