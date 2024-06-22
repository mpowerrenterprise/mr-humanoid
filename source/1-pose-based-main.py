import cv2
import mediapipe as mp
import math
import numpy as np
import time
from pyfirmata import Arduino, util

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

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(2)

# Initialize the minimum and maximum distance values for left and right hands
min_distance_left = float('inf')
max_distance_left = 0
min_distance_right = float('inf')
max_distance_right = 0

# Initiate holistic model
with mp_holistic.Holistic(min_detection_confidence=0.3, min_tracking_confidence=0.3) as holistic:

    while cap.isOpened():
        ret, frame = cap.read()

        # Recolor Feed
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Make Detections
        results = holistic.process(image)

        # Recolor image back to BGR for rendering
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.pose_landmarks:  # Check if body landmarks are detected
            # Pose Detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

            # Extract left wrist (landmark 15) and left hip (landmark 23) coordinates
            left_wrist = results.pose_landmarks.landmark[15]
            left_hip = results.pose_landmarks.landmark[23]

            # Extract right wrist (landmark 24) and right hip (landmark 18) coordinates
            right_wrist = results.pose_landmarks.landmark[24]
            right_hip = results.pose_landmarks.landmark[18]

            # Assuming you know the dimensions of the image
            image_width = frame.shape[1]
            image_height = frame.shape[0]

            # Convert normalized coordinates to pixels for left hand
            left_wrist_x_pixel = int(left_wrist.x * image_width)
            left_wrist_y_pixel = int(left_wrist.y * image_height)
            left_hip_x_pixel = int(left_hip.x * image_width)
            left_hip_y_pixel = int(left_hip.y * image_height)

            # Convert normalized coordinates to pixels for right hand
            right_wrist_x_pixel = int(right_wrist.x * image_width)
            right_wrist_y_pixel = int(right_wrist.y * image_height)
            right_hip_x_pixel = int(right_hip.x * image_width)
            right_hip_y_pixel = int(right_hip.y * image_height)

            # Calculate the Euclidean distance in pixels for left hand
            distance_in_pixels_left = math.sqrt((left_wrist_x_pixel - left_hip_x_pixel)**2 + (left_wrist_y_pixel - left_hip_y_pixel)**2)

            # Calculate the Euclidean distance in pixels for right hand
            distance_in_pixels_right = math.sqrt((right_wrist_x_pixel - right_hip_x_pixel)**2 + (right_wrist_y_pixel - right_hip_y_pixel)**2)

            # Update minimum and maximum distances for left hand
            if distance_in_pixels_left < min_distance_left:
                min_distance_left = distance_in_pixels_left
            if distance_in_pixels_left > max_distance_left:
                max_distance_left = distance_in_pixels_left

            # Update minimum and maximum distances for right hand
            if distance_in_pixels_right < min_distance_right:
                min_distance_right = distance_in_pixels_right
            if distance_in_pixels_right > max_distance_right:
                max_distance_right = distance_in_pixels_right

            # Calculate the updated range based on the minimum and maximum distances for left hand
            min_range_left = min_distance_left
            max_range_left = max_distance_left

            # Calculate the updated range based on the minimum and maximum distances for right hand
            min_range_right = min_distance_right
            max_range_right = max_distance_right

            # Calculate the midpoint of the line for left hand
            midpoint_x_left = (left_wrist_x_pixel + left_hip_x_pixel) // 2
            midpoint_y_left = (left_wrist_y_pixel + left_hip_y_pixel) // 2

            # Calculate the midpoint of the line for right hand
            midpoint_x_right = (right_wrist_x_pixel + right_hip_x_pixel) // 2
            midpoint_y_right = (right_wrist_y_pixel + right_hip_y_pixel) // 2

            # Draw a pink line between left wrist and left hip
            cv2.line(image, (left_wrist_x_pixel, left_wrist_y_pixel), (left_hip_x_pixel, left_hip_y_pixel), (255, 0, 255), 2)

            # Draw a blue circle at the center of the line for left hand
            cv2.circle(image, (midpoint_x_left, midpoint_y_left), 8, (255, 0, 0), -1)  # -1 to fill the circle

            # Draw a pink line between right wrist and right hip
            cv2.line(image, (right_wrist_x_pixel, right_wrist_y_pixel), (right_hip_x_pixel, right_hip_y_pixel), (255, 0, 255), 2)

            # Draw a blue circle at the center of the line for right hand
            cv2.circle(image, (midpoint_x_right, midpoint_y_right), 8, (255, 0, 0), -1)  # -1 to fill the circle

            # Calculate the rotation angle for left hand
            rotation_value_left = np.interp(int(distance_in_pixels_left), [min_range_left, max_range_left],[180, 0])

            # Calculate the rotation angle for right hand
            rotation_value_right = np.interp(int(distance_in_pixels_right), [min_range_right, max_range_right],[0, 180])

            # Control the left and right hand rotation using the Arduino
            left_hand.write(rotation_value_left)
            right_hand.write(rotation_value_right)

        cv2.imshow('Raw Webcam Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Allow time for the servos to move to the positions
time.sleep(2)  # Adjust time as needed


board.exit()
cap.release()
cv2.destroyAllWindows()
