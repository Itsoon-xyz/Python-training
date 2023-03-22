allowedResponse = ["y", "yes", "n", "no"]
answer = "y"
validInput = False
error = "Invalid input please enter only y, yes, n, no"

while not validInput:
    validInput = False
    while not validInput:
        year = input("Enter your age :")
        if year.isnumeric():
            validInput = True
        else:
            print("Please enter only an integer number!!!")

    validInput = False
    while not validInput:
        birth = str(input("Your birthday came this year? (y/n) :"))
        if birth.lower() in allowedResponse:
            if birth.lower() in ["y", "yes"]:
                calc = 2023
            else:
                calc = 2022
            validInput = True
        else:
            print(error)

    calc = calc - int(year)
    print("You are born on ", calc)
    validInput2 = False
    while not validInput2:
        answer = input("You want restart? (y/n) :")
        if answer.lower() in allowedResponse:
            if answer.lower() in ["y", "yes"]:
                validInput = False
                continue
            else:
                print("GoodBye")
                break
