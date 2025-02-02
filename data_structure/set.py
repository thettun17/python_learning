guests = {"Thet Tun", "Aung Aung", "Maung Maung"}
print(guests)  # {'Thet Tun', 'Aung Aung', 'Maung Maung'}
# print(guests[0]) # TypeError: 'set' object is not subscriptable


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection
print(set1 & set2)  # {4, 5}

# Difference
print(set1 - set2)  # {1, 2, 3}