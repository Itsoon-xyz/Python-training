import time

answer = "y"
while answer == "y":
    try:
        year = int(input("Enter your age :"))
        if year <= 0:
            print("Please enter only an integer number!!!")
            continue
    except:
        print("Please enter only number!!!")
        continue

    try:
        birth = str(input("You celebrated your birthday this year? (y/n) :"))
        if birth == "y" or "n":
            if birth == "y":
                calc = 2023
            else:
                calc = 2022
    except:
        print("Jsp")

    calc = calc - year
    print("You are born on " + str(calc))
    time.sleep(0.5)
    answer = str(input("You want restart? (y/n) :"))
    if answer in "y" or "n":
        if answer == "n":
            print("Goodbye")
