import asyncio
from pyfirmata import Arduino, util
import time
import websockets

# Define the serial port (check your Arduino IDE for the correct port)
port = 'COM3'  # Change 'COM3' to your Arduino's serial port

# Create a new Arduino board instance
board = Arduino(port)

# Define the LED pin (e.g., pin 13)
servo_pin = board.get_pin('d:13:s')  # Digital output pin 13
 
# create handler for each connection
 
async def handler(websocket, path):
 
    data = await websocket.recv()
    print(data)

    if data == "[NORMAL]":
        servo_pin.write(0)

    elif data == "[CENTER]":
        servo_pin.write(90)
    
    elif data == "[FULL]":
        servo_pin.write(180)

    

 
    #reply = f"Data recieved as: {data}!"
    #await websocket.send(reply)
 
start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
 
asyncio.get_event_loop().run_forever()

board.exit()