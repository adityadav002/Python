def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Aditya", "Rohan", "Aan", "and"]
print(rem(l, "an"))