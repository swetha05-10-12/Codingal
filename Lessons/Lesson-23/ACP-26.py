num=int(input("Enter a number:"))
num_list=[]
for i in range (num+1):
    if i%2!=0:
        num_list.append(i)
print(num_list)

fruits=["apple","banana","tomato","strawberry","cherry"]
print(fruits)

for i in range (6):
    fruits.append(fruits.capitalize())


print(fruits)
