# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

def task2():
    num = int(input("Введите число: "))
    dc = []
    n = 1
    for i in range(1, num+1):
        n = n * i
        dc.append(n)
    return dc

print(task2())