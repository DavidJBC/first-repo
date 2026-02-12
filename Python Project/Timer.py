import time

print("This project is a timer project")

minute = int(input("Enter how many minutes you want in the timer: "))
seconds = int(input("Enter how many seconds you want in the timer: "))

timer = (minute * 60) + seconds

print("Timer is set to " + str(minute) + " minute(s) and " + str(seconds) + " second(s)") 

time.sleep(timer)

print(".....done")