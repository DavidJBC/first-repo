print ("Pick an Operation")
print("Addition, Subtraction, Multiplication, Division")

Op = input("Operation  ")


def Addition():
    
    num1ad = int(input("Enter Your First Number "))
    num2ad = int(input("Enter Your Second Number "))

    resultad = num1ad + num2ad

    print(str(num1ad) + " + " + str(num2ad) + " = " + str(resultad))
    
def Subtraction():

    num1s = int(input("Enter Your First Number "))
    num2s = int(input("Enter Your Second Number "))

    results = num1s - num2s

    print(str(num1s) + " - " + str(num2s) + " = " + str(results))

def Multiplication():

    num1x = float(input("Enter Your First Number "))
    num2x = float(input("Enter Your Second Number "))

    resultx = num1x * num2x

    print(str(num1x) + " * " + str(num2x) + " = " + str(resultx))

def Division():
    
    num1d = float(input("Enter Your First Number "))
    num2d = float(input("Enter Your Second Number "))

    resultd = num1d / num2d

    print(str(num1d) + " * " + str(num2d) + " = " + str(resultd))



if  Op == "Addition":
    Addition()
elif Op == "Subtraction":
    Subtraction()
elif Op == "Multiplication":
    Multiplication()
elif Op == "Division":
    Division()
elif  Op == "addition":
    Addition()
elif Op == "subtraction":
    Subtraction()
elif Op == "multiplication":
    Multiplication()
elif Op == "division":
    Division()
elif  Op == "ADDITION":
    Addition()
elif Op == "SUBTRACTION":
    Subtraction()
elif Op == "MULTIPLICATION":
    Multiplication()
elif Op == "DIVISION":
    Division()
else:
    print("Choose a Proper Operation")