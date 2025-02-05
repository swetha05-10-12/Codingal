print("Welcome to the quiz game!")
name=input("Enter your name:")
age=int(input("Enter your age:"))
if age<11 or age>15:
    print("Sorry",name,"you cant take the quiz!")
elif age<=0 :
    print("Please enter your real age!")
else:
    print("You can take the quiz! ")
    print("Quiz options:")
    print("1.The Anagram Room ")
    print("2.The Puzzle Room ")
    print("3.The Mental Maths Room ")

    choice=int(input("Enter the number of the quiz you want to attempt:"))

    def anagram():
        print("An anagram is a word or phrase formed by rearranging the letters of another word or phrase. All the original letters must be used exactly once, but they can be in any order.")
        print("Q1.Rearrange the letters of 'LISTEN' to form a meaningful word")
        print("a)TENSIL")
        print("b)ENLIST")
        print("c)STENSIL")
        print("d)INLEST")
        ANS1=("Enter the letter of your answer:")
        if ANS1=="a" or ANS1=="A":
            print("Correct answer!")
        else:
            print("Sorry! Incorrect answer! The correct answer was option a.")
        print("Q2.What is an anagram of 'TEACH'?")
        print("a)HECTA")
        print("b)CHEAT")
        print("c)TACHA")
        print("d)CHETA")
        ANS2=("Enter the letter of your answer:")
        if ANS2=="b" or ANS2=="B":
            print("Correct answer!")
        else:
            print("Sorry! Incorrect answer! The correct answer was option b.")
        print("Q3.Which word is an anagram of 'CINEMA'?")
        print("a)MACHINE")
        print("b)ANEMIC")
        print("c)CAMINE")
        print("d)MINCEA")
        ANS3=("Enter the letter of your answer:")
        if ANS3=="b" or ANS3=="B":
            print("Correct answer!")
        else:
            print("Sorry! Incorrect answer! The correct answer was option b.")
        print("Q4.Find the anagram of 'SPARE'")
        print("a)REAPS")
        print("b)PEARS")
        print("c)PARSE")
        print("d)ALL OF THE ABOVE")
        ANS4=("Enter the letter of your answer:")
        if ANS4=="d" or ANS4=="D":
            print("Correct answer!")
        else:
            print("Sorry! Incorrect answer! The correct answer was option d.")
        print("Q5.What is the anagram of 'EVIL'?")
        print("a)LIVE")
        print("b)VEIL")
        print("c)VILE")
        print("d)ALL OF THE ABOVE")
        ANS5=("Enter the letter of your answer:")
        if ANS5=="d" or ANS5=="D":
            print("Correct answer!")
        else:
            print("Sorry! Incorrect answer! The correct answer was option d.")
if choice==1:
    anagram()