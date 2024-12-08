english=int(input("Enter your marks for English:"))
if english<0:
    print("Invalid input! Mark will be considered 0")
    english=0
math=int(input("Enter your marks for Math:"))
if math<0:
    print("Invalid input! Mark will be considered 0")
    math=0
science=int(input("Enter your marks for Science:"))
if science<0:
    print("Invalid input! Mark will be considered 0")
    science=0
hindi=int(input("Enter your marks for Hindi:"))
if hindi<0:
    print("Invalid input! Mark will be considered 0")
    hindi=0
tamil=int(input("Enter your marks for Tamil:"))
if tamil<0:
    print("Invalid input! Mark will be considered 0")
    tamil=0
mark=english+math+science+hindi+tamil
percentage=(mark/500)*100
if percentage>95:
    print("Your grade is O (Outstanding)!")
elif percentage>=91 and percentage<=95:
    print("Your grade is A1")
elif percentage<=90 and percentage>=81:
    print("Your grade is A2")
elif percentage<=80 and percentage>=71:
    print("Your grade is B1")
elif percentage<=70 and percentage>=61:
    print("Your grade is B2")
elif percentage<=60 and percentage>=51:
    print("Your grade is C1")
elif percentage<=50 and percentage>=41:
    print("Your grade is C2")
elif percentage<=40 and percentage>=31:
    print("Your grade is D1")
elif percentage<=30 and percentage>=21:
    print("Your grade is D2")
else:
    print("You failed")

if english==0:
    print("You failed English")
if math==0:
    print("You failed Math")
if science==0:
    print("You failed Science")
if hindi==0:
    print("You failed Hindi")
if tamil==0:
    print("You failed Tamil")