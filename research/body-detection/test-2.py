import cv2
import mediapipe as mp
import numpy as np
import math
import pyautogui  # To control the system volume

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(0)

# Initiate holistic model
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()

        # Recolor Feed
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Make Detections
        results = holistic.process(image)

        # Recolor image back to BGR for rendering
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Calculate the distance between landmarks 4 (THUMB_TIP) and 8 (INDEX_FINGER_TIP)
        if results.left_hand_landmarks:
            thumb_tip = results.left_hand_landmarks.landmark[15].x, results.left_hand_landmarks.landmark[15].y
            index_finger_tip = results.left_hand_landmarks.landmark[23].x, results.left_hand_landmarks.landmark[23].y

            distance = math.sqrt((thumb_tip[0] - index_finger_tip[0])**2 + (thumb_tip[1] - index_finger_tip[1])**2)

            # Calculate the volume percentage and limit it to the range [0, 99]
            volume_percentage = int(distance * 99)  # Convert to a 2-digit number (00 to 99)
            volume_percentage = max(0, min(99, volume_percentage))  # Limit it to [0, 99]

            # Convert the volume_percentage to a 2-digit string
            volume_percentage_str = f"{volume_percentage:02}"

            # Adjust the system volume (you may need to use a system-specific method)
            # For example, using PyAutoGUI:
            # pyautogui.press("volumedown", presses=volume_percentage)  # Decrease volume

            print(f"Volume Percentage: {volume_percentage_str}")

        # Draw landmarks
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

        cv2.imshow('Raw Webcam Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
