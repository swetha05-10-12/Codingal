BW=int(input("Enter the number of black and white pages:"))
CO=int(input("Enter the number of colour pages:"))

def cost(BW,CO):
    total=BW*2+CO*5
    print("Total amount to be paid: Rs.",total)

cost(BW,CO)
