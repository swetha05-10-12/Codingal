num1=int(input("Enter the starting number of the range of the numbers you want to find a square for:"))

num2=int(input("Enter the ending number of the range of the numbers you want to find a square for:"))

squares=[]

for i in range (num1,num2+1):
    squares.append(i*i)

print(squares)
