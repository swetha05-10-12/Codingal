age = int(input("Enter your age: "))
if age>18:
    print("You are eligible to vote")
elif age<18 and age>0:
    print("You are not eliglible to vote")
else:
    print("Please enter a proper age")