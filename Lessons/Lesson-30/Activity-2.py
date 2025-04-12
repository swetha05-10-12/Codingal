class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
    
flash=[]
print("Wecome to the flashcard application!")

while(True):
    word=input("Enter the word you want on the flashcard:")
    meaning=input("Enter the meaning of your word:")

    flash.append(flashcard(word,meaning))
    option=int(input("If you want to add one moe flashcard, enter 0, or else, enter 1:"))

    if (option):
        break
print("\nYour flashcards:")
for i in flash:
    print(">",i)