# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением
# дробной части элементов.

price =[1.1, 1.2, 3.1, 5, 10.01]
lst = []
for i in range(len(price)):
    if price[i] % 1 != 0:
        inp = round(price[i] - int(price[i]), 2)
        lst.append(inp)
print(lst)

myMax = lst[0]
myMin = lst[0]

for i in range(len(lst)):
    if lst[i] > myMax : myMax = lst[i]
    if lst[i] < myMin : myMin = lst[i]

print ('Max:', myMax, 'Min:', myMin, 'Разница: ', myMax - myMin)
