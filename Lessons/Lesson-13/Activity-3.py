def add(P,Q):
    return P+Q
def sub(P,Q):
    return P-Q
def mul(P,Q):
    return P*Q
def div(P,Q):
    return P/Q

print("Operations:")
print("a.Addition")
print("b.Subtraction")
print("c.Multiplication")
print("d.Division")
choice=input("Enter your choice:")
num_1=int(input("Enter the first number:"))
num_2=int(input("Enter the sceond number:"))
if choice=="a" or choice=="A":
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice=="b" or choice=="B":
    print(num_1,"-",num_2,"=",sub(num_1,num_2))
elif choice=="c" or choice=="C":
    print(num_1,"*",num_2,"=",mul(num_1,num_2))
elif choice=="d" or choice=="D":
    print(num_1,"/",num_2,"=",div(num_1,num_2))
else:
    print("Invalid input.")