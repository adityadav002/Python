# Without walrus operator
data = input("Enter something: ")
while data != "exit":
    print(f'You entered: {data}')
    data = input("Enter something: ")

# With walrus operator
while (data := input("Enter something: ")) != "exit":
    print(f'You entered: {data}')



