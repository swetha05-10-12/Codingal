choice=input("Would you like to shut down your program?:")
def shutdown(choice):
    if choice=="yes" or choice=="Yes":
        print("Shutting down.")
    elif choice=="no" or choice=="No":
        print("Aborting shut down.")
    else:
        print("Sorry")

shutdown(choice)