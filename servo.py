# Set up libraries and overall settings
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical layout
GPIO.setwarnings(False)

# Set up pin 11 for PWM
GPIO.setup(03,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
pwn = GPIO.PWM(03, 50)     # Sets up pin 11 as a PWM pin
pwn.start(0)               # Starts running PWM on the pin and sets it to 0
def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(03, True)
	pwn.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(03, False)
	pwn.ChangeDutyCycle(0)
set = input("Set your angle: ")
SetAngle(set)

# Clean up everything
pwn.stop()                 # At the end of the program, stop the PWM
GPIO.cleanup()           # Resets the GPIO pins back to defaults
