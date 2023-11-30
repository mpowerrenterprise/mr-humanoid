import speech_recognition as sr
from pyfirmata import Arduino, util

# Define the serial port (check your Arduino IDE for the correct port)
port = 'COM3'  # Change 'COM3' to your Arduino's serial port

# Create a new Arduino board instance
board = Arduino(port)

# Define the LED pin (e.g., pin 13)
servo_pin = board.get_pin('d:13:s')  # Digital output pin 13

while True:
    rec = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 1  # Increase pause threshold
        audio = rec.listen(source, phrase_time_limit=5)

    try:
        print("Processing...")
        spoken_text = rec.recognize_google(audio, language='en')
        print(spoken_text)

        if "hands up" in spoken_text.lower():  # Test with a known phrase
            servo_pin.write(180)
        elif "hands in the middle" in spoken_text.lower():
            servo_pin.write(90)
        elif "hands down" in spoken_text.lower():
            servo_pin.write(0)


   
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

board.exit()
