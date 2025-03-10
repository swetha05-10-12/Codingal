test_dict={"Codingal":3,"is":2,"best":2,"for":2,"Coding":1}
print(test_dict)

user_choice=int(input("Enter the value that you want to check the frequency of:"))

frequency=0

for key in test_dict:
    if test_dict[key]==user_choice:
        frequency=frequency+1

print("The frequency of",user_choice,"is:",frequency)