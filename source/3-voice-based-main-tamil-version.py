import time
import speech_recognition as sr
from pyfirmata import Arduino, util

# Initialize the recognizer
recognizer = sr.Recognizer()

# Define the serial port (check your Arduino IDE for the correct port)
port = 'COM3'  # Change 'COM3' to your Arduino's serial port

# Create a new Arduino board instance
board = Arduino(port)

# Allow time for the board to initialize
time.sleep(2)

# Define the LED pins for left and right hands (e.g., pin 13 for left hand, pin 9 for right hand)
left_hand = board.get_pin('d:13:s')  # Digital output pin 13
right_hand = board.get_pin('d:12:s')  # Digital output pin 12
head = board.get_pin('d:11:s')  # Digital output pin 11

left_hand.write(180)
right_hand.write(0)
head.write(90)

while True:

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)
        #audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='ta-LK')
            print("Recognizing...")
            dataText = format(text)
            dataText = dataText.strip()

            print(f"Out: {dataText}")

            if "வலது கையை தூக்கவும்" in dataText or "வலது கையை மேல் நோக்கி உயர்த்தவும்" in dataText or "வலது கையை மேல் நோக்கி தூக்கவும்" in dataText or "வலது கையை உயர்த்தவும்" in dataText or "வலது கையை மேல் நோக்கி எழுப்பவும்" in dataText or "வலது பக்க கையை உயர்த்தவும் " in dataText or " கையை உயர்த்தவும்" in dataText or "வலது பக்க கையை மேல் நோக்கி உயர்த்தவும்" in dataText:
                right_hand.write(180)


            if "இடது கையை தூக்கவும்" in dataText or "இடது கையை மேல் நோக்கி உயர்த்தவும்" in dataText or "இடது கையை மேல் நோக்கி தூக்கவும்" in dataText or "இடது கையை உயர்த்தவும்" in dataText or "இடது கையை மேல் நோக்கி எழுப்பவும்" in dataText or "இடது பக்க கையை உயர்த்தவும்" in dataText or "இடது பக்க கையை உயர்த்தவும் " in dataText or "இடது பக்க கையை மேல் நோக்கி உயர்த்தவும்" in dataText:
                left_hand.write(0)

            if "வலது கையை கீழே இரக்கவும்" in dataText or "வலது கையை கீழ் நோக்கி இரக்கவும்" in dataText or "வலது கையை கீழே விடவும்" in dataText or "வலது கையை கீழே பதிக்கவும்" in dataText or "வலது கையை கீழ் நோக்கி விடவும்" in dataText or "வலது பக்க கையை பதிக்கவும் " in dataText or " வலது பக்க கையை கீழ் நோக்கி இரக்கவும்" in dataText or "வலது பக்க கையை இரக்கவும்" in dataText:
                right_hand.write(0)

            if "இடது கையை கீழே இரக்கவும்" in dataText or "இடது கையை கீழ் நோக்கி இரக்கவும்" in dataText or "இடது கையை கீழே விடவும்" in dataText or "இடது கையை கீழே பதிக்கவும்" in dataText or "இடது கையை கீழ் நோக்கி விடவும்" in dataText or "இடது பக்க கையை பதிக்கவும் " in dataText or " இடது பக்க கையை கீழ் நோக்கி இரக்கவும்" in dataText or "இடது பக்க கையை இரக்கவும்" in dataText:
                left_hand.write(180)

            elif "கைகளை உயர்த்தவும்" in dataText or "கைகளை தூக்கவும்" in dataText or "கைகளை மேலே தூக்கவும்" in dataText or "கைகளை மேலே உயர்த்தவும்" in dataText or "இரண்டு கைகளையும் மேலே கொண்டு செல்லவும்" in dataText or "இரு கைகளையும் மேலே உயர்த்தவும்" in dataText:
                left_hand.write(0)
                right_hand.write(180)

            elif "கைகளை இரக்கவும்" in dataText or "கைகளை கீழே விடவும்" in dataText or "கைகளை விடவும்" in dataText or "கைகளை மேலே உயர்த்தவும்" in dataText or "இரண்டு கைகளையும் கீழ் நோக்கி கொண்டு செல்லவும்" in dataText or "இரு கைகளையும் பதிக்கவும்" in dataText:
                left_hand.write(180)
                right_hand.write(0)

            elif "இடது பக்கம் தலையை திருப்பவும்" in dataText or "இடது பக்கம் தலையை நகர்த்தவும்" in dataText or "தலையை இடதுபக்கம்திருப்பவும்" in dataText or "இட பக்கம் தலையை நகர்த்தவும்" in dataText or "இட பக்கம் தலையை திருப்பவும்" in dataText or "தலையை இட பக்கம்திருப்பவும்" in dataText or "தலையை இட பக்கம் கிறுக்கவும்" in dataText or "தலையை இடது பக்கம் கிறுக்கவும்" in dataText :
                head.write(180)

            elif "வலது பக்கம் தலையை நகர்த்தவும்" in dataText or "வலது பக்கம் தலையை திருப்பவும்" in dataText or "தலையை வலது பக்கம்திருப்பவும்" in dataText or "தலையை வலது பக்கம் கிறுக்கவும்" in dataText or "வல பக்கம் தலையை நகர்த்தவும்" in dataText or "வல பக்கம் தலையை திருப்பவும்" in dataText or "வல பக்கம் தலையை திருப்பவும்" in dataText or "தலையை வல பக்கம்திருப்பவும்" in dataText or "தலையை வல பக்கம் கிறுக்கவும்" in dataText :
                head.write(0)

            elif "நேரே பார்க்கவும் " in dataText or "முன் நோக்கி பார்க்கவும்" in dataText or "தலையை முன் நோக்கி பார்க்கவும்" in dataText or "தலையை முன் பக்கம் வைக்கவும்" in dataText:
                head.write(90)

        except Exception as e:
            print(e)


# Allow time for the servos to move to the positions
time.sleep(2)  # Adjust time as needed      

board.exit()
