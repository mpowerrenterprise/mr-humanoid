import cv2
import mediapipe as mp
import numpy as np
import math

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

# Initialize the camera and the holistic model
cap = cv2.VideoCapture(0)

known_distance = None
known_hand_size_pixels = None

calibrating = True  # Set to True initially to enter calibration mode

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            continue

        # Recolor the frame
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Make detections
        results = holistic.process(image)

        # Recolor the frame back to BGR for rendering
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if calibrating:
            # Display calibration instructions
            cv2.putText(image, "Place hand at known distance and size", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            if results.left_hand_landmarks:
                thumb_tip = results.left_hand_landmarks.landmark[4]
                index_finger_tip = results.left_hand_landmarks.landmark[8]

                # Calculate the size of the hand in pixels
                hand_size_pixels = abs(thumb_tip.x - index_finger_tip.x) * frame.shape[1]

                if known_distance is None:
                    # Measure and set the known distance once
                    known_distance = float(input("Enter the known distance (in centimeters): "))

                # Update known_hand_size_pixels during calibration
                known_hand_size_pixels = hand_size_pixels

                # Exit calibration mode after the first measurement
                calibrating = False

        elif results.left_hand_landmarks:
            thumb_tip = results.left_hand_landmarks.landmark[4]
            index_finger_tip = results.left_hand_landmarks.landmark[8]

            # Calculate the size of the hand in pixels
            hand_size_pixels = abs(thumb_tip.x - index_finger_tip.x) * frame.shape[1]

            # Calculate the calibration factor
            calibration_factor = known_distance / known_hand_size_pixels

            # Calculate the distance from the camera
            distance = hand_size_pixels * calibration_factor

            # Display the distance on the frame
            cv2.putText(image, f"Distance: {distance:.2f} cm", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Draw landmarks
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

        cv2.imshow('Hand Distance Measurement', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
