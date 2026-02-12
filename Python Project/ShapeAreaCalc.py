print("=========================")
print("     Area Calculator")
print("=========================")

print("1) Square")
print("2) Rectangle")
print("3) Triangle")
print("4) Circle")
shape = int(input("Pick a shape: "))

if shape == 1:
    side = float(input("Measurement of the side: "))
    result = side * side
    print("The are of the square is " + str(result))
elif shape == 2:
    width = float(input("Measurement of the wodth: "))
    lenght = float(input("Measurement of the lenght"))
    result = width * lenght
    print("The area of the rectangle is " + str(result))
elif shape == 3:
    base = float(input("Measurement of the base: "))
    height = float(input("Measurment of the heaight: "))
    result = (height * base) * 0.5
    print("The area of the triangle is " + str(result))
elif shape == 4:
    radius = float(input("Measurement of the radius: "))
    pi = 3.14
    result = (radius * radius) * pi
    print("The area of the circle is " + str(result))
