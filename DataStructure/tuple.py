# Tuple are immutable, ordered collection of items just like list but cannot be modified (i.e. you cannot change its content).

# Creating a Tuple
tuple = ("apple", "banana", "cherry")

# Accessing a Tuple
print(tuple)
print(tuple[0])
print(tuple[-1])

from collections import namedtuple
# Named Tuple
Student = namedtuple('Student', ['name', 'age', 'DOB'])
S = Student("Aung Aung", 20, '1999-01-01')
print(S.name)