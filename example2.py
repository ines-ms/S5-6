import random
drinks = ["vodka", "tequila", "rum", "gin", "mezcal",]
try:
    name = input("What is your name?")
    age = input("How old are you?")
    age = int(age)
    nationality = input("Where are you from?")
except ValueError:
    print("Invalid age. Please enter a number.")
else:
    if age < 0 or age >140:
        print("You are not human. This is a game for humans only")
    elif age > 120:
        print("You are to old to play the awesome drinking game")
    elif age < 18:
        print("You are a minor. You can't play the awesome drinking game.")
    elif nationality == "USA" or nationality == "UAE"  and age < 21:
        print("You are not allowed to drink in USA or UAE. You can'st play this drinking game")
    else:
        print("You are an adult. You can play the awesome drinking game")
        print("Have some", random.choice(drinks), "and you enjoy the game.")