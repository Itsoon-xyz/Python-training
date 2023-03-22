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

    try:
        validInput = False
        while not validInput:
            birth = str(
                input("You celebrated your birthday this year? (y/n) :"))
            if birth.lower() in allowedResponse:
                if birth.lower() in ["y", "yes"]:
                    calc = 2023
                else:
                    calc = 2022
                validInput = True
            else:
                print("Invalid input. Please enter y, yes, n, or no.")

    except:
        print("Jsp")

    calc = calc - year
    print("You are born on ", calc)
    validInput = False
    while not validInput:
        answer = str(input("You want restart? (y/n) :"))
        if answer.lower() in allowedResponse:
            if answer not in ["y", "yes"]:
                print("Goodbye")
            validInput = True
        else:
            print("Invalid input. Please enter y, yes, n, or no.")
