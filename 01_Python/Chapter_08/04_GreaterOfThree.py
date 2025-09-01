def great(a, b, c):
    if(a>b and a>c):
        print("A is grestest.")
    elif(b>c and b>a):
        print("B is greatest.")
    else:
        print("C is greatest.")

a = int(input("Enter a Number: "))
b = int(input("Enter a Number: "))
c = int(input("Enter a Number: "))

great(a, b, c)