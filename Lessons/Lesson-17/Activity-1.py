import random
playing=True
number=str(random.randint(10,20))
print("I will generate a number from 10 to 20, and you should try to guess the one digit number.")
print("The game is over when you win by guessing the number right.")
while playing:
    guess = input("Enter your number that you guessed:")
    if number==guess:
        print("You Win!")
        print("The number was",number)
        break
    else:
        print("Sorry! Your guess wasn't correct")

'''import random #importing module

playing = True #initialise

number = str(random.randint(10,20)) #random in-built function


print("I will generate a number from 10 to 20, and you have to guess the number one digit at a time.")

print("The game ends when you get 1 hero!")

#iterate loop till the condition is true

while playing:

    guess = input("Give me your best guess! \n")

    if number == guess:

        print("You win the game")

        print("The number was",number)

        break


    else:

        print("Your guess isn't quite right, try again. \n")'''


        
