# List is a collection of items in a particular order.
# List is Mutable.

# ************** List Creation **************

Objects = ["Ben", 10, True, "Aditya", 12.34]
print(Objects)
print(Objects[0])
print(Objects[1])
print(Objects[2])
print(Objects[3])
print(Objects[4])

print()

# ************************ List Methods ************************* 
# (Change, Add, Remove, Insert, Delete, Clear)

Objects[2] = False  # Change True to False.
print(Objects)

print()

Objects.append("Aditya Yadav")  # Add "Aditya Yadav" to the list.
print(Objects)

print()

Objects.remove("Ben")  # Remove "Ben" from the list.
print(Objects)

print()

Objects.insert(0, "Aditya Yadav")  # Insert "Aditya Yadav" at index 0.
print(Objects)

print()

del Objects[0]  # Delete "Aditya Yadav" from the list.
print(Objects)

print()

Objects.clear()  # Clear the list.
print(Objects)

print()

Objects = ["Ben", 10, True, "Aditya", 12.34]
Objects.pop()  # Remove the last item from the list.
print(Objects)

print()

Objects = ["Ben", 10, True, "Aditya", 12.34]
Objects.pop(1)  # Remove the item at index 1 from the list.
print(Objects)

print()

Objects = ["Ben", 10, True, "Aditya", 12.34]
Objects.reverse()  # Reverse the order of the list.
print(Objects)

print()

object = [34, 12, 56, 2, 45]
object.sort()  # Sort the list in ascending order.
print(object)

print()

object = [34, 12, 56, 2, 45]
object.sort(reverse=True)  # Sort the list in descending order.
print(object)

print()
