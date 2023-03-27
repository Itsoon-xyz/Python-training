import random

# def
attempt = 1
bestAttempt = 0
allowedResponse = ["y", "yes", "n", "no"]


validInput = False
while not validInput:
    print("The number is between 0 and 100.")
    gnumber = random.randrange(0, 100)
    print(gnumber)
    win = False
    while not win:
        quest = False
        while not quest:
            ask = input("What the number:")
            if ask.isnumeric():
                ask = int(ask)
            else:
                print("Please enter only an integer number!!!")
            if ask == gnumber:
                print(f"You win the number is {gnumber}.")
                print(f"In {attempt} attempt.")
                win = True
                quest = True
                if bestAttempt < attempt:
                    bestAttempt == attempt
                    print(f"Best attempt is {bestAttempt}.")
            else:
                if ask > gnumber:
                    print("More low")
                else:
                    print("More hight")
                    attempt += 1

    validInput = False
    while not validInput:
        question = input("You want restart? (y/n) :")
        if question.lower() in allowedResponse:
            if question.lower() in ["y", "yes"]:
                break
            else:
                print("GoodBye")
                validInput = True
        else:
            print("Invalid input please enter only y, yes, n, no.")
