a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
choice_3=input("Do you wish to add a third number(Yes/No):")
if choice_3=="No" or choice_3=="no":
    print("Addition=", a + b)
    print("Subtraction=", a - b)
    print("Division=", a / b)
    print("Multiplication=", a * b)
    if a>b:
        print("Number 1 is greater than Number 2")
    elif b>a:
        print("Number 2 is greater than Number 1")
    else:
        print("Number 1 and Number 2 are equal")
elif choice_3=="Yes" or choice_3=="yes":
    c=int(input("Enter number 3:"))
    print("Addition=", a + b + c)
    print("Subtraction=", a - b - c)
    print("Division=", a / b /c)
    print("Multiplication=", a * b * c)
    if a>b:
        if a>c:
            print("Number 1 is greater than Number 2 and 3")
        else:
            print("Number 1 is greater than Number 2. Number 3 is greater than Number 1")
    elif b>a:
        if b>c:
            print("Number 2 is greater than Number 1 and 3")
        else:
            print("Number 2 is greater than Number 1. Number 3 is greater than Number 2")
    else:
         print("All numbers ar equal")
else:
    print("Invalid input!")

    
