num=int(input("Enter a number:"))
num_list=[]
for i in range (num+1):
    if i%2!=0:
        num_list.append(i)
print(num_list)

fruits = ["apple", "banana", "tomato", "strawberry", "cherry"]
print("Original List:", fruits)

for i in range(len(fruits)):
    fruits[i] = fruits[i].capitalize()

print("Capitalized List:", fruits)


print(fruits)
