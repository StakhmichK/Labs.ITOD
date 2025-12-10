tea_list = ['oolong', 'herbal', 'black tea', 'oolong']
tea_set = set(tea_list)
print("1:", tea_set)

A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print("2:", sum(A) == sum(B))

letters = ['A', 'B', 'C', 'A', 'B', 'C']
letters_set = set(letters)
print("3:", letters_set)

S = {'A', 'B', 'C'}
S.add('D')
print("4:", S)

A_set = {1, 2, 3, 4, 5}
B_set = {1, 3, 9, 12}
intersection = A_set.intersection(B_set)
print("5:", intersection)

dino_set1 = set(["T-Rex", "Triceratops", "Velociraptor"])
dino_set2 = set(["Velociraptor", "Brachiosaurus", "Stegosaurus"])
dino_set3 = dino_set1.union(dino_set2)
print("6:", dino_set3)

print("7:", dino_set1.issubset(dino_set3))

D = {'a': 0, 'b': 1, 'c': 2}
print("8:", D)

print("9:", D['a'])
print("10:", D.keys())

soundtrack_dic = {
    "Dragon Quest: Awakening": "2015",
    "Lost in the Nebula": "2021"
}
print("11:", soundtrack_dic)

print("12:", soundtrack_dic.keys())
print("13:", soundtrack_dic.values())

dino_popularity = {
    "T-Rex": 95,
    "Velociraptor": 88,
    "Triceratops": 90
}
print("14:", dino_popularity)

print("15:", dino_popularity["T-Rex"])
print("16:", dino_popularity.keys())
print("17:", dino_popularity.values())
