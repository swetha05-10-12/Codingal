tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

print(tup1)
print(tup2)

product1 = 1 
product2 = 1  

for i in tup1:
    product1 *= i 

for i in tup2:
    product2 *= i 

print("Product of tup1:", product1)
print("Product of tup2:", product2)