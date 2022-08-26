# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.

num = input("Введите число: ")
if num.isdigit() == True:
    n = int(num)
    suma = 0
    while n > 0:
        digit = n % 10
        suma = suma + digit
        n = n // 10
    print("Сумма:", suma)
else:
    x = num.split(".")
    # print(x)
    a = int(x[0]) # целая часть
    b = int(x[1]) # дробная часть
    mult = 1
    while (a != 0):
        mult = mult + (a % 10)
        a = a // 10
    while (b != 0):
        mult = mult + (b % 10)
        b = b // 10
    print("Сумма цифр равна:", mult)