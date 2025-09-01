l = [11, 21, 31, 41, 51]

# without enumberate
# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# with enumberate
for index, item in enumerate(l):
     print(f"The item number at index {index} is {item}")