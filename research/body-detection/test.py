import cv2
import mediapipe as mp
import math
import numpy as np
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

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(0)

# Initiate holistic model
with mp_holistic.Holistic(min_detection_confidence=0.3, min_tracking_confidence=0.3) as holistic:

    while cap.isOpened():
        ret, frame = cap.read()

        # Recolor Feed
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Make Detections
        results = holistic.process(image)
        # print(results.face_landmarks)

        # Recolor image back to BGR for rendering
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.pose_landmarks:  # Check if body landmarks are detected
            # Pose Detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

            # Extract left wrist (landmark 15) and left hip (landmark 23) coordinates
            left_wrist = results.pose_landmarks.landmark[15]
            left_hip = results.pose_landmarks.landmark[23]

            # Assuming you know the dimensions of the image
            image_width = frame.shape[1]
            image_height = frame.shape[0]

            # Convert normalized coordinates to pixels
            left_wrist_x_pixel = int(left_wrist.x * image_width)
            left_wrist_y_pixel = int(left_wrist.y * image_height)
            left_hip_x_pixel = int(left_hip.x * image_width)
            left_hip_y_pixel = int(left_hip.y * image_height)

            # Calculate the Euclidean distance in pixels
            distance_in_pixels = math.sqrt((left_wrist_x_pixel - left_hip_x_pixel)**2 + (left_wrist_y_pixel - left_hip_y_pixel)**2)

            # Calculate the midpoint of the line
            midpoint_x = (left_wrist_x_pixel + left_hip_x_pixel) // 2
            midpoint_y = (left_wrist_y_pixel + left_hip_y_pixel) // 2

            # Draw a pink line between left wrist and left hip
            cv2.line(image, (left_wrist_x_pixel, left_wrist_y_pixel), (left_hip_x_pixel, left_hip_y_pixel), (255, 0, 255), 2)

            # Draw a blue circle at the center of the line
            cv2.circle(image, (midpoint_x, midpoint_y), 8, (255, 0, 0), -1)  # -1 to fill the circle

            # Print the distance in pixels
            #print("Distance between left wrist and left hip (in pixels):", int(distance_in_pixels))

            rotation_value = np.interp(int(distance_in_pixels), [70, 430], [0, 180])

            servo_pin.write(rotation_value)

            print(f"Value: {rotation_value}")

            

        cv2.imshow('Raw Webcam Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

board.exit()
cap.release()
cv2.destroyAllWindows()
