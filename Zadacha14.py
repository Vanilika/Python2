#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
number = int(input("Введите число: "))
for i in range(1, number):
    dva = 2 ** i
    if dva >= number:
        break
    print(dva)