# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
n = input('Enter number N = ')
z = n.replace(',', '')
sum_item = 0
print(list(z))
for item in list(z):
    item = int(item)
    sum_item = item + sum_item
print(sum_item)
