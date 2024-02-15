a = int(input("Сколько чисел Фибониаччи Вам вывести? "))
Fib1 = 0
Fib2 = 1
print(Fib1)
print(Fib2)
i = 2
b = 1
while i < a:
    s = Fib1 + Fib2
    print(s)
    Fib1 = Fib2
    Fib2 = s
    i = i + 1 