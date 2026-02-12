print("Let's check if your number is even  or odd")
number = int(input("Enter your number here: "))

result = number % 2

if result != 0:
    print("Your number is odd")
else:
    print("Your number is even")