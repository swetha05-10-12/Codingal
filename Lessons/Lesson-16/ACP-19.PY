try:
    age=int(input("Enter your age:"))
except ValueError as ex:
    print("Exception",ex)
else:
    if age%2==0:
        print("Yor age is an even number.")
    else:
        print("Your age is an odd number.")
