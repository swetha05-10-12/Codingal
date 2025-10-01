print("Even Number Checker:")
num=int(input("Enter your number:"))
def even(num):
    if num%2==0:
        return "True"
    else:
        return "False"
    
print("True=Even")
print("False=Odd")
print(num,"is",even(num))