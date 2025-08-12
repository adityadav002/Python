# Initial set with mixed data types
s = {1, 2, 3, 5, "Aditya"}

# Add a new element
s.add(4)
print("After adding 4:", s)

# Add a duplicate element (no effect)
s.add(4)
print("After trying to add duplicate 4:", s)

# Add multiple elements using update()
s.update([5, 6])  # 5 is duplicate; 6 is new
print("After update with [5, 6]:", s)

# Remove an element (raises error if not found)
s.remove(2)
print("After removing 2:", s)

# Discard an element (safe even if not found)
s.discard(10)
print("After discarding 10 (not present):", s)

# Pop a random element
popped = s.pop()
print(f"Popped element: {popped}")
print("After pop:", s)

# Clear the entire set
s.clear()
print("After clear:", s)
