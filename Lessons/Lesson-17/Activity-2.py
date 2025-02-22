def compute_hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            hcf=i
    return hcf
num1=120
num2=360

print("The HCF(Highest Common Factor) is:", compute_hcf(num1,num2))