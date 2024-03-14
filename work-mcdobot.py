# Methods Exercise
# Kate Jiang
# 2/22/2024

question = input("Would you like fries with your meal? (Yes/No)")

if question.lower().strip() == "yes":
    print("Here's your meal with fries!")
elif question.lower().strip() == "no":
    print("Here's your meal without fries!")
else:
    print(f"Sorry, I don't understand {question}")
