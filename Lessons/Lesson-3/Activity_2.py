Amount=int(input("Please enter amount for withdraw :"))

note_1=Amount//100
note_2=(Amount%100)//50
note_3=((Amount%100)%50)//10

print("notes of 100 ruppee: ", note_1)
print("notes of 50 ruppee: ", note_2)
print("notes of 10 ruppee: ", note_3)