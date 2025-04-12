import random
class Fruit_quiz:
    def __init__(self):

        self.fruits={'apple':'red','orange':'orange','watermelon':'green','banana':'yellow'}

    def quiz(self):
        while (True):

            fruit,colour=random.choice(list(self.fruits.items()))

            print("What is the colour of {}?".format(fruit))

            user_answer=input()

            if user_answer.lower()==colour:
                print("Correct answer!")
            else:
                print("Wrong answer")

            option=int(input("Enter 0 if you wnat to play again, enter 1 if you want to stop:"))

            if(option):
                break

print("Welcome to the fruit quiz!")
F_q=Fruit_quiz()
F_q.quiz()