cost_price=int(input("Enter the cost price:"))
selling_price=int(input("Enter the selling price:"))
if cost_price<selling_price:
    print("You have a profit")
elif cost_price==selling_price:
    print("You have neither had a profit nor a loss")
else:
    print("You have had a loss")
