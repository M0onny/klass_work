#codin: utf-8
#Задача 1 
A = int(input("Введите первое число: "))
B = int(input("Введите второе число: "))
if A > B:
    maximum = A 
    minimum = B
else: 
    maximum = B 
    minimum = A
print("Максимальное число: ", maximum)
print ("Минимальное число: ", minimum)

#Задача 2
a = int(input("Введите сторону: "))
b = int(input("Введите радиус: "))
if b > a:
    print("Не впишется")
else:
    print("Впишется")
    
#Задание 4
a = int(input("Введите сторону: "))
b = int(input("Введите радиус: "))
if a < b:
    print("Квадрат влез: ")
else:
    print("Квадрат невлез: ")

#Задание 5
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    print("Первое число больше")
else:
    print("Второе число больше")