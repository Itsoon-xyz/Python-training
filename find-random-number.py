import random

attempt = 1
allowedResponse = ["y", "yes", "n", "no"]

validInput = False
while not validInput:
    verifnumber = False
    while not verifnumber:
        n1 = input("First number :")
        if n1.isnumeric():
            n1 = int(n1)
            verifnumber = True
        else:
            print("Invalid input. Please enter only an integer number!!!")
    verifnumber = False
    while not verifnumber:
        n2 = input("Second number :")
        if n2.isnumeric():
            n2 = int(n2)
            if n2 > n1:
                verifnumber = True
            else:
                print("Invalid input. Please set second number superior to the first.")
        else:
            print("Invalid input. Please enter only an integer number!!!")

    print(f"The number is between {n1} and {n2}.")
    gnumber = random.randrange(n1, n2)
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
            else:
                attempt += 1
                if ask > gnumber:
                    print("More low")
                else:
                    print("More hight")

    validInput = False
    while not validInput:
        question = input("You want restart? (y/n) :")
        if question.lower() in allowedResponse:
            if question.lower() in ["y", "yes"]:
                attempt = 1
                break
            else:
                print("GoodBye")
                validInput = True
        else:
            print("Invalid input please enter only y, yes, n, no.")
