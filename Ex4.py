# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Enter number N = '))
lst = []
multiply = 1
sum_item = 0
for i in range (-n, n + 1):
    lst.append(i)
print(lst)
with open ('file.txt', 'r') as my_file:
    data = my_file.read()
new_lst = data.split()
print(new_lst)

for item in new_lst:
    item = int(item)
    multiply = lst[item] * multiply
    print (lst[item])
print(multiply)
