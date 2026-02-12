print("This is a tip calculator")

bill = int(input("Enter the total amount of bill: "))
tip_amount = int(input("Enter the percentage you want to tip: "))

tip_percentage = tip_amount * 0.01

total_tip = bill * tip_percentage

print("The tip is " + str(total_tip))

