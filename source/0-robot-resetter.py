from pyfirmata import Arduino, util
import time

# Define the serial port (check your Arduino IDE for the correct port)
port = 'COM3'  # Change 'COM3' to your Arduino's serial port

# Create a new Arduino board instance
board = Arduino(port)

# Allow time for the board to initialize
time.sleep(2)

# Define the pins for the servos
left_hand = board.get_pin('d:13:s')  # Digital output pin 13 for servo
right_hand = board.get_pin('d:12:s')  # Digital output pin 12 for servo
head = board.get_pin('d:11:s')  # Digital output pin 11 for servo

# Move the servos to the desired positions
left_hand.write(180)
right_hand.write(0)
head.write(90)

# Allow time for the servos to move to the positions
time.sleep(2)  # Adjust time as needed

# Close the connection to the board
board.exit()
