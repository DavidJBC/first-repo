import random

dices = int(input("How many dice you want to use? "))

probability = random.randint(dices, dices * 6)

print("You got " + str(probability) + " from a probability of " + str(dices) + "-" + str(dices * 6)) 