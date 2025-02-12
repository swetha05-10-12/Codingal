#login and home page
print("Welcome to the quiz game!")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
def choice():
        print("Quiz options:")
        print("1. The Anagram Room")
        print("2. The Puzzle Room")
        print("3. The Mental Maths Room")
        return int(input("Enter the number of your choice: "))

#play again?
def retry():
    ans = input("Would you like to play again? (Yes/No): ")
    if ans == "yes" or ans=="Yes":
        q_choice = choice()  
        if q_choice == 1:
            anagram()
        elif q_choice == 2:
            Puzzle()
        elif q_choice == 3:
            Mental_maths()
        else:
            print("Please enter a valid option!")
            retry()  
    elif ans.lower() == "no":
        print("Thanks for playing!")
    else:
        print("Enter a valid option please")
        retry()

   
#anagram
def anagram():
    score=0
    print("Welcome to The Anagram Room!")
    print("An anagram is a word or phrase formed by rearranging the letters of another word or phrase. All the original letters must be used exactly once, but they can be in any order. Good luck!")
    print("Q1.Rearrange the letters of 'LISTEN' to form a meaningful word")
    print("a)TENSIL")
    print("b)ENLIST")
    print("c)STENSIL")
    print("d)INLEST")
    ANS1=input("Enter the letter of your answer:")
    if ANS1=="a" or ANS1=="A":
        print("Correct answer!")
        score=score+1
    else:
        print("Sorry! Incorrect answer! The correct answer was option a.")
    print("Q2.What is an anagram of 'TEACH'?")
    print("a)HECTA")
    print("b)CHEAT")
    print("c)TACHA")
    print("d)CHETA")
    ANS2=input("Enter the letter of your answer:")
    if ANS2=="b" or ANS2=="B":
        print("Correct answer!")
        score=score+1
    else:
        print("Sorry! Incorrect answer! The correct answer was option b.")
    print("Q3.Which word is an anagram of 'CINEMA'?")
    print("a)MACHINE")
    print("b)ANEMIC")
    print("c)CAMINE")
    print("d)MINCEA")
    ANS3=input("Enter the letter of your answer:")
    if ANS3=="b" or ANS3=="B":
            print("Correct answer!")
            score=score+1
    else:
            print("Sorry! Incorrect answer! The correct answer was option b.")
    print("Q4.Find the anagram of 'SPARE'")
    print("a)REAPS")
    print("b)PEARS")
    print("c)PARSE")
    print("d)ALL OF THE ABOVE")
    ANS4=input("Enter the letter of your answer:")
    if ANS4=="d" or ANS4=="D":
            print("Correct answer!")
            score=score+1
    else:
        print("Sorry! Incorrect answer! The correct answer was option d.")
    print("Q5.What is the anagram of 'EVIL'?")
    print("a)LIVE")
    print("b)VEIL")
    print("c)VILE")
    print("d)ALL OF THE ABOVE")
    ANS5=input("Enter the letter of your answer:")
    if ANS5=="d" or ANS5=="D":
        print("Correct answer!")
        score=score+1
    else:
        print("Sorry! Incorrect answer! The correct answer was option d.")
    final_score=score*2
    print("You have totaly scored:",final_score,"/10")
    print (retry())
#mental maths
def Mental_maths():
        score=0
        print("Welcome to The Mental Maths Room!")
        print("These are 5 mental maths questions that test your ability to think logically and solve Math problmes, inside your head! Good luck!")
        q1=int(input("What is 25*8?:"))
        if q1==int(200):
            ("Correct answer!")
            score=score+1
        else:
            print("Sorry!Wrong!")
        q2=int(input("A book costs ₹120. If you buy 3 books, how much will you pay?:"))
        if q2==int(360):
            ("Correct answer!")
            score=score+1
        else:
            print("Sorry!Wrong!")
        q3=int(input("What is the vaue of 72 ÷ 9 + 5 * 2?:"))
        if q3==int(16):
            ("Correct answer!")
            score=score+1
        else:
            print("Sorry!Wrong!")
        q4=int(input("If 15 percent of a number is 45, what is the number?:"))
        if q4==int(300):
            ("Correct answer!")
            score=score+1
        else:
            print("Sorry!Wrong!")
        q5=int(input("What is the sum of the angles in a triangle?:"))
        if q5==int(180):
            ("Correct answer!")
            score+1
        else:
            print("Sorry!Wrong!")

        final_score=score*2
        print("You have totaly scored:",final_score,"/10")
        print(retry())
#puzzle
def Puzzle():
        score=0
        print("Welcome to The Puzzle Room!")
        print("These puzzles are 5 tricky and fun questions designed to challenge logic, reasoning, and lateral thinking. The questions cover riddles and common sense puzzles. Answer in one word only, and good luck!")
        q1=input("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?")
        if q1=="echo" or q1=="Echo":
            print("Correct answer!")
            score=score+1
        else:
            print("Sorry!Wrong!")
        q2=input("The more you take, the more you leave behind. What am I?")
        if q2=="footsteps" or q2=="Footsteps":
            print("Correct answer!")
            score=score+1
        else:
            print("Sorry!Wrong!")
        q3=input("The more it dries, the wetter it gets. What is it?")
        if q3=="Towel" or q3=="towel":
            print("Correct answer!")
            score=score+1
        else:
            print("Sorry!Wrong!")
        q4=input("I have a head and a tail, but no body. What am I?")
        if q4=="Coin" or q4=="coin":
            print("Correct answer!")
            score=score+1
        else:
            print("Sorry!Wrong!")
        q5=input("The person who makes it sells it. The person who buys it never uses it. The person who uses it never knows they are using it. What is it?")
        if q5=="Coffin" or q5=="coffin":
            print("Correct answer!")
            score=score+1
        else:
            print("Sorry!Wrong!")
        final_score=score*2
        print("You have totaly scored:",final_score,"/10")
        print(retry())
if age < 11 and age>0 or age > 15:
        print("Sorry", name, "you can't take the quiz!")
elif age<=0:
        print("That is not a real age!")
        print (age())
else:
        print("You can take the quiz!")
        q_choice=choice()
        if q_choice == 1:
            anagram()
        elif q_choice == 2:
            Puzzle()
        elif q_choice == 3:
            Mental_maths()
        else:
            print("Please enter a valid option!")