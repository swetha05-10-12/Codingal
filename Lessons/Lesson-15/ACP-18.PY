amnt_paid=int(input(("Enter the amount you paid in total:")))
bill=int(input("Enter the actual cost of your bill:"))
def due_amnt(amnt_paid,bill):
    return amnt_paid - bill

print("Your change is:",due_amnt(amnt_paid,bill))