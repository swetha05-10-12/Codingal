name=input("Enter your name:")
age=input("Enter your age:")
health=input("Describe your health (Good/Bad):")
weight=input("Enter you weight in kgs:")
height=input("Enter you height in cm:")
if health=="Good":
    if height>90:
        if weight<120:
            if age>=50 and age<60:
                print("You can go on all the rides")
            elif age>=8 and age<15:
                print("You cant go on the Sky Pendellum and the Dare Drop")
            elif age==16 and age<=58:
                print("You can go on all the rides")
            elif age>=4 and age<8:
                print("You can go only for bungee jumping")
            else:
                print("You cant go on any rides")
        else:
            print("You are not eligible for any rides")
            
    else:
        print("You are not eligible for any rides")   
        
else:
    print("You are not eligible fro any rides")
    