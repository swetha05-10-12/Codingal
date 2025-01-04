number=int(input("Enter a number:"))
print("Number=", number)
temp_number=number
print("Temp_number=",temp_number)
sum=0
while temp_number!=0:
    digit=temp_number%10
    sum = sum + digit
    temp_number = temp_number//10

print("The sum of the number is:",sum)