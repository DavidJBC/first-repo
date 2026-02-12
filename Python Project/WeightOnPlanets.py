
weight = float(input("What is your weight on earth? "))
planet = int(input("Select a planet using the numbers for 1-7 "))

mc_relativeGravity = 0.38
v_relativeGravity = 0.91
ma_relativeGravity = 0.38
j_relativeGravity = 2.53
s_relativeGravity = 1.07
u_relativeGravity = 0.89
n_relativeGravity = 1.14

if planet == 1:
  result = weight * mc_relativeGravity
  world = "Mercury"
elif planet == 2:
  result = weight * v_relativeGravity
  world = "Venus"
elif planet == 3:
  result = weight * ma_relativeGravity
  world = "Mars"
elif planet == 4:
  result = weight * j_relativeGravity
  world = "Jupiter"
elif planet == 5:
  result = weight * s_relativeGravity
  world = "Saturn"
elif planet == 6:
  result = weight * u_relativeGravity
  world = "Uranus"
elif planet == 7:
  result = weight * n_relativeGravity
  world = "Neptune"
else:
  world = 1
  
if world != 1:
  print("Your weight on planet " + world + " is "+ str(result))
else:
  print("Invalid")