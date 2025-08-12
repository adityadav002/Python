# Tuple is Immutable.

a = (1, "Aditya", True, 12.34)
print(a)

print()

# ************************ Tuple Methods ************************* 

my_tuple = (10, 20, 30, 40)
print(my_tuple.index(30))  # Output: 2

my_tuple = (10, 20, 20, 30)
print(my_tuple.count(20))  # Output: 2

my_tuple = (1, 2, 3)
print(len(my_tuple))  # Output: 3

t = (5, 1, 9)
print(min(t))  # Output: 1
print(max(t))  # Output: 9
