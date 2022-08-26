# Задайте список из N элементов, заполненных числами из
# промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиций может быть более двух, пользователь вводит индексы с клавиатуры


n = int(input('Введите количество чисел в диапазоне: '))
numbers = []
input_value = input('Введите числа, разделенные пробелом: ').split()
print(input_value)

for i in range(-n, n):
    numbers.append(i)

a, b, *args = input_value
a = int(a)
b = int(b)
c = int(*args)
get = numbers[a] * numbers[b] * numbers[c]
# print(numbers[a])
# print(numbers[b])
# print(numbers[c])
print(get)

# print(numbers)
