from Tkinter import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

# Make sure all LEDs are off at the start of this program
GPIO.output(21, GPIO.LOW)
GPIO.output(20, GPIO.LOW)
GPIO.output(16, GPIO.LOW)

win = Tk()
win.title("Red Yellow Green")

def redOn():
	GPIO.output(21, GPIO.HIGH)	# Turn on red
	GPIO.output(20, GPIO.LOW)	# Turn off yellow
	GPIO.output(16, GPIO.LOW)	# Turn off green

def yellowOn():
	GPIO.output(21, GPIO.LOW)	# Turn off red
	GPIO.output(20, GPIO.HIGH)	# Turn on yellow
	GPIO.output(16, GPIO.LOW)	# Turn off green

def greenOn():
	GPIO.output(21, GPIO.LOW)	# Turn off red
	GPIO.output(20, GPIO.LOW)	# Turn off yellow
	GPIO.output(16, GPIO.HIGH)	# Turn on green

def close():
	GPIO.cleanup()
	win.destroy()

var = IntVar()

radioRed = Radiobutton(win, text = "Red LED", variable = var, value = 1, command = redOn)
radioRed.pack()

radioYellow = Radiobutton(win, text = "Yellow LED", variable = var, value = 2, command = yellowOn)
radioYellow.pack()

radioGreen = Radiobutton(win, text = "Green LED", variable = var, value = 3, command = greenOn)
radioGreen.pack()

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()
