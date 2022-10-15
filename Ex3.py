# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
n = int(input('Enter number N = '))
lst = []
i = 1
sum = 0
for i in range (1, n + 1):
    num = (1 + 1/i)**i
    sum = num + sum
    lst.append(num)
print(sum)