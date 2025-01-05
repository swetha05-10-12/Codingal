a=int(input("Enter the start value:"))
b=int(input("Enter the end value:"))
num=int(input("Enter the number to find its multiples:"))
num2=num
print("You want the find the multiples of:",num2)
for i in range(a,b+1):
    if i%num==0:
        print(i)