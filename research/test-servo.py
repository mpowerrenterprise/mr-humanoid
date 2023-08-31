from pyfirmata import Arduino, util
import time

# Define the serial port (check your Arduino IDE for the correct port)
port = 'COM3'  # Change 'COM3' to your Arduino's serial port

# Create a new Arduino board instance
board = Arduino(port)
# Define the servo pin (e.g., pin 9)
servo_pin = board.get_pin('d:13:s')  # Digital output pin 9, configured as servo

# Set the servo to its initial position
servo_pin.write(90)  # 90 degrees (center position)

# Wait for a few seconds
time.sleep(2)

# Move the servo to a different position
servo_pin.write(0)  # 0 degrees (leftmost position)

# Wait for a few seconds
time.sleep(2)

# Move the servo to another position
servo_pin.write(180)  # 180 degrees (rightmost position)

# Wait for a few seconds
time.sleep(2)

# Close the board connection
board.exit()
