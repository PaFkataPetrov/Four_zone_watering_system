import RPi.GPIO as GPIO
import time
import tkinter as tk

# Set up GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)  # Humidity sensor for area 1
GPIO.setup(11, GPIO.IN)  # Humidity sensor for area 2
GPIO.setup(13, GPIO.IN)  # Humidity sensor for area 3
GPIO.setup(15, GPIO.IN)  # Humidity sensor for area 4

GPIO.setup(16, GPIO.OUT)  # Water pump for area 1
GPIO.setup(18, GPIO.OUT)  # Water pump for area 2
GPIO.setup(22, GPIO.OUT)  # Water pump for area 3
GPIO.setup(24, GPIO.OUT)  # Water pump for area 4

# Initialize GUI
root = tk.Tk()
root.title("Automatic Watering System")

# Create label for humidity readings
humidity_label = tk.Label(root, text="Humidity: ")
humidity_label.grid(row=0, column=0)


# Define function to update humidity label
def update_humidity():
    humidity1 = GPIO.input(7)
    humidity2 = GPIO.input(11)
    humidity3 = GPIO.input(13)
    humidity4 = GPIO.input(15)

    humidity_label.config(text="Humidity: {}/{}/{}/{}".format(humidity1, humidity2, humidity3, humidity4))

    root.after(1000, update_humidity)


# Define function to water each area
def water_area(area_num, pump_pin):
    print("Watering area {}".format(area_num))
    GPIO.output(pump_pin, GPIO.HIGH)
    time.sleep(5)  # Water for 5 seconds
    GPIO.output(pump_pin, GPIO.LOW)


# Create buttons to water each area
button1 = tk.Button(root, text="Water Area 1", command=lambda: water_area(1, 16))
button1.grid(row=1, column=0)

button2 = tk.Button(root, text="Water Area 2", command=lambda: water_area(2, 18))
button2.grid(row=1, column=1)

button3 = tk.Button(root, text="Water Area 3", command=lambda: water_area(3, 22))
button3.grid(row=2, column=0)

button4 = tk.Button(root, text="Water Area 4", command=lambda: water_area(4, 24))
button4.grid(row=2, column=1)

# Call update_humidity function to start updating the humidity label
update_humidity()

# Run GUI
root.mainloop()

# Clean up GPIO pins
GPIO.cleanup()