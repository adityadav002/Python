a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a.union(b))                   # {1, 2, 3, 4, 5}
print("Intersection:", a.intersection(b))     # {3}
print("Difference:", a.difference(b))         # {1, 2}
print("Symmetric Difference:", a.symmetric_difference(b))  # {1, 2, 4, 5}
