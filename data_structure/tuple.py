# coordinate = (1, 2, 3)
# # Unpacking
# x, y, z = coordinate
# print(x, y)

# # Immutable
# numbers = (1, 2, 3, 5)
# numbers[3] = 4
# print(numbers)


scores = (1, 2, 3, 4, 5)
winner, *others = scores
print(winner)
print(others)
