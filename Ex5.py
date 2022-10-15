# Реализуйте алгоритм перемешивания списка.

lst1 = [6, 5, 5, 9, 10, 75, 45]
lst2 = [1, 10, 12, 7, 3, 41, 50]
print(lst1)
print(lst2)
temple = 1
for item in range(len(lst1)):
    if lst2[item] > lst1[item]:
        temple = lst2[item]
        lst2[item] = lst1[item]
        lst1[item] = temple        

print("Change lists")
print(lst1)
print(lst2)

