def ageCalc():
    print("This is an age calculator")
    birth_year = int(input("What is the year that you were born? "))
    current_year = int(input("What is the current year? "))

    result = current_year - birth_year

    print("Your are approximately " + str(result) + " years old")

ageCalc()