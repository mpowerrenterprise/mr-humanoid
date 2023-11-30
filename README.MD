# Mr. Humanoid

## Repo Structure

```
    ├── docs                                   # Contains documents.
    ├── research                               # Contains pre-research experiments.
    │   ├── 0-code-references                      # Contains reference codes.
    │   ├── 1-web-based-prototype-v1.0.0           # Contains a web app trained using Teachable Machine.
    │   ├── 2-desktop-based-prototype-v1.0.0       # Contains py apps basic prototypes.
    ├── source                                 # Contains main source code.
    │   ├── 0-pose-based-main.py                   # pose-based version
    │   ├── 1-voice-based-main.py                  # voice-based version
    └── README.MD                              # Readme Content.

```

## 01 Introduction

It is a humanoid robot powered by Arduino and AI, responding to humans' poses and voice commands. This robot has two significant features: it can work with human postures, mimic arm movements, listen to humans, and move its arms and head according to voice inputs.

![Circuit Diagram](docs/media/3-banner-image.png)

## 02 Technology Stack

### 2.1 Hardware Stack

- Arduino UNO (1)
- 180deg Micro Servo Motor (3)
- Full / Half Bread Board (1)
- Jumper Wires

### 2.2 Software Stack

- Python 3.8.5
- Arduino IDE (Framework)
- OpenCV
- Mediapipe 0.10.3
- PyFirmata
- SpeechRecognition
- PyAudio

## 03 Setup

### 3.1 Hardware Setup

![Circuit Diagram](docs/media/0-circuit-diagram.png)

| Objects       | Pin No  |
| ------------- | ------- |
| **Left Arm**  | Pin: 13 |
| **Right Arm** | Pin: 12 |
| **Head**      | Pin: 11 |

### 3.2 Firmware Setup

Setting up the Arduino firmware is necessary to enable communication between Python and Arduino. The Firmata protocol establishes serial communication between a Python script and an Arduino.

To upload Firmata, open Arduino IDE and choose the correct COM port and **file -> Examples -> Firmata -> StandardFirmata -> Upload to Arduino UNO Board**.

![Firmware Setup](docs/media/1-firmware-setup.png)

**Note:** After uploading StandardFirmata to the Arduino Board, Python can be used to program it.

### 3.3 Setup Software

We will now install the necessary software and configure the AI to gain access to the Arduino Board. This project utilizes essential libraries, including Speech Recognition, MediaPipe, and OpenCV. We need to install all the required dependencies on the development computer.

- **Step 01:** Install Python

  ```
  Ver: 3.8.5 is Recommended (www.python.org)
  ```

- **Step 02:** Navigate to the specified location in CMD/Terminal.

  ```
  mr-humanoid/docs/requirements.txt
  ```

- **Step 03:** Execute the given command to install all dependencies.

  ```
  pip install -r requirements.txt
  ```

## 04 Usage

We have two Python programs: **0-pose-based-main.py (Pose-based)** and **1-voice-based-main.py (Voice-based)**:

- **Pose-based:** This program utilizes OpenCV and MediaPipe to track and mimic the movement of a human arm.

- **Voice-based:** This program utilizes Speech Recognition technology to listen to human voices and carry out instructions.

- **Source Directory:**

  ```
  mr-humanoid\source

      * 0-pose-based-main.py
      * 1-voice-based-main.py
  ```

### 4.1 Setps to run

- **Step 01:** Connect the Arduino to the development computer.

- **Step 02:** Modify the script to reflect the appropriate COM port.

  ![Change COM Port](docs/media/2-change-com-port.png)

- **Step 03:** To run the Pose-based app.

  ```
  python 0-pose-based-main.py
  ```

- **Step 04:** To run the Voice-based app.

  ```
  python 1-voice-based-main.py
  ```

### 4.2 Output

<img src="docs/media/4-output-pose-1.gif" alt="Output Pose 1" width="100%">

![Output Pose 2](docs/media/5-output-pose-2.jpg)

![Output Pose 3](docs/media/6-output-pose-3.jpg)

![Output Voice 1](docs/media/7-output-voice.jpg)

### 4.2 Voice Commands

| Voice Commands      |
| ------------------- |
| **right hand up**   |
| **left hand up**    |
| **right hand down** |
| **left hand down**  |
| **hands up**        |
| **hands down**      |
| **head left**       |
| **head right**      |
| **head forward**    |

## Social Links

- [Linkedin Profile](https://www.linkedin.com/in/gunarakulangunaretnam)
- [Facebook Profile](https://www.facebook.com/gunarakulangunaratnam)
- [Instagram Profile](https://www.instagram.com/gunarakulangunaretnam)
- [Twitter Profile ](https://twitter.com/gunarakulangr)
- [Kaggle Profile](https://www.kaggle.com/gunarakulangr)
- [TikTok Profile](https://www.tiktok.com/@gunarakulangunaretnam)
- [Youtube Profile](https://www.youtube.com/channel/UCMWkED5sabgVZSCKjZuRJXA)
