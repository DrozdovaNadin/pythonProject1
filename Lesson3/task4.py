# Напишите программу, которая будет преобразовывать десятичное число в двоичное.


def bin(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s


print(bin(45))
print(bin(3))
print(bin(2))