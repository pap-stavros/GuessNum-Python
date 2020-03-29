import random

while True:

    #Generates the random integer.
    random_integer = (random.randint(1, 20))

    #Receives input from the user.
    guess = input("Guess the number from 1 - 20!\n")
    Tries = 0


    #Success:
    if guess == (random_integer):
        random_integer = str(random_integer)
        Tries = str(Tries)
        print("You've Won!")
        print("It only took you " + Tries + " times!")
        break

    #Fail:
    if guess != random_integer:
        random_integer = str(random_integer)
        print("The number was:" + " " + random_integer)
        print("Try again..\n")
        Tries = Tries + 1