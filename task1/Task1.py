# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#
# Примеры:
#
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90
i = 1
mylist = []
while i <= 5:
    a = int(input())
    mylist.append(a)
    i+=1
print(max(mylist))