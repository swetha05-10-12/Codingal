try:
    number = int(input("Enter a number:"))
    print("The number entered is", number)
except ValueError as ex:
    print("Exeption:",ex)