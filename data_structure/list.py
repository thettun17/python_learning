numbers = [4, 2, 3, 1, 9, 5, 7, 8, 6, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number

print(f'maxium number is {max}') 


duplicate_number = [2, 2, 6, 1, 3, 6, 3, 4, 5, 4]
unique = []
for no in duplicate_number:
    if no not in unique:
        unique.append(no)
print(unique)