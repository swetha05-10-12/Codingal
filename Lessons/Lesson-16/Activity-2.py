try:
    num1,num2=eval(input("Enter 2 numbers, and separate them with a comma:"))
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("Division by zero results in an error!")

except SyntaxError:
    print("The comma to separate the two numbers entered are missing!")

except:
    print("Wrong input!")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")