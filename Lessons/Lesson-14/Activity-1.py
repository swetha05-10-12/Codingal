def total_calc(bill_amount,tip):
    total = bill_amount*(1+0.01*tip)
    total= round(total)
    print(f"Please pay $",total)

total_calc(300,27)