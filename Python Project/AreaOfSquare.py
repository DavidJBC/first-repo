#---------------------------------------------------------------------------------------
#Planes
def Square():
    plane_sides = float(input("Enter The Measurement of The side of The Square "))

    SquareArea = plane_sides * plane_sides

    print("The Area of The Square is " + str(SquareArea))

def Triangle():
    base = float(input("Enter The Measurement of The base of The Triangle"))
    height = float(input("Enter The Measurement of The Height of The Triangle"))

    Triangle_Area = (base * height) * 0.5
    print(Triangle_Area)

def Rectangle():
    Lenght = float(input("Enter The Measurement of The Lenght of The Rectangle"))
    Width = float(input("Enter The Measurement of The Width of The Rectangle"))

    RectangleArea = Lenght * Width

    print(RectangleArea)

def Circle():
    Radius = float(input("Enter The Measurement of The Radius of The Circle"))
    Pi = 3.14

    AreaCircle = (Radius * Radius) * Pi

    print(AreaCircle)
#---------------------------------------------------------------------------------------
#3D

def Cube():
    Side3 = float(input("Enter The Measurement of The Side of The Cube"))

    CubeArea = Side3 * Side3 * Side3

    print(CubeArea)

def RectangularPrism():
    Lenght = float(input("Enter The Measurement of The Lenght of The Rectangular Prism"))
    Width = float(input("Enter The Measurement of The Width of The Rectangular Prism"))
    Height = float(input("Enter The Measurement of The Height of The Rectangular Prism"))

    AreaRP = Lenght * Width * Height

    print(AreaRP)

    

Conv = input("What shape do you want to calculate")

if Conv == "Square":
    Square()
elif Conv == "Triangle":
    Triangle()