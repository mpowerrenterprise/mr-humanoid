import speech_recognition as sr
from pyfirmata import Arduino, util

# Initialize the recognizer
recognizer = sr.Recognizer()

# Define the serial port (check your Arduino IDE for the correct port)
port = 'COM3'  # Change 'COM3' to your Arduino's serial port

# Create a new Arduino board instance
board = Arduino(port)

left_hand = board.get_pin('d:13:s')  # Digital output pin 13
right_hand = board.get_pin('d:9:s')  # Digital output pin 9
head = board.get_pin('d:11:s')  # Digital output pin 9

left_hand.write(0)
right_hand.write(170)
head.write(90)

while True:

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)
        #audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("Recognizing...")
            dataText = format(text)
            dataText = dataText.strip()

            print(f"Out: {dataText}")

            if "right hand up" in dataText:
                right_hand.write(0)

            elif "left hand up" in dataText:
                left_hand.write(180)

            elif "right hand down" in dataText:
                right_hand.write(170)

            elif "left hand down" in dataText:
                left_hand.write(0)

            elif "hands up" in dataText or "handsome" in dataText:
                left_hand.write(180)
                right_hand.write(0)

            elif "hands down" in dataText:
                left_hand.write(0)
                right_hand.write(170)

            elif "head left" in dataText:
                head.write(180)

            elif "head right" in dataText or "headlight" in dataText:
                head.write(0)

            elif "head forward" in dataText:
                head.write(90)


        except Exception as e:
            print(e)
            

board.exit()
