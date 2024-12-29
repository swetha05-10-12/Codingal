start=int(input("Enter a start value:"))
end=int(input("Enter an end value:"))
step=int(input("Enter a step value:"))
for i in range(end):
    print(i)
print("Starting a new loop")
for i in range(start,end):
    print(i)
print("Starting a new loop")
for i in range(start,end,step):
    print(i)