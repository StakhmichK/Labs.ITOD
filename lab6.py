A = (0, 1, 2, 3)
first_two_A = A[:2]
print("Перші два елементи A:", first_two_A)

heroes_tuple = ("Batman", "Superman", "Wonder Woman", "Flash",
"Iron Man", "Spider-Man", "Hulk", "Thor")
len_heroes = len(heroes_tuple)
print("Довжина heroes_tuple:", len_heroes)
print("Елемент з індексом 3:", heroes_tuple[3])

slice_345 = heroes_tuple[3:6]
print("Елементи 3, 4, 5:", slice_345)

first_two_heroes = heroes_tuple[:2]
print("Перші два персонажі:", first_two_heroes)
thor_index = heroes_tuple.index("Thor")
print("Індекс 'Thor':", thor_index)

C_tuple = (-5, 1, -3)
sorted_C = sorted(C_tuple)
print("Відсортований список:", sorted_C)

a_list = [1, "hello", [1, 2, 3], True]
print("Елемент з індексом 1:", a_list[1])
slice_a = a_list[1:4]
print("Елементи 1-3:", slice_a)

A_list = [1, "a"]
B_list = [2, 1, "d"]
merged = A_list + B_list
print("Об'єднання списків:", merged)

B = ["a", "b", "c"]
print("Перші два елементи B:", B[:2])

B[0] = "A"
print("Оновлений список B:", B)