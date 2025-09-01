try:   # if this successfully works goes inside the else, otherwise except.
    a = int(input('Enter a number: '))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else")