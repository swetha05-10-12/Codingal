print("Floyd's triangle:")
r=int(input("Enter the number of rows for your triangle:"))
number=1
for i in range(1,r+1):
    for j in range(1,i+1):
        print(number,end="")
        number = number +1
    print()
