# MR.HUMANOID

## Repo Structure

```
    ├── docs                                   # Contains documents.
    ├── research                               # Contains pre-research experiments.
    │   ├── 0-code-references                      # Contains reference codes.
    │   ├── 1-web-based-prototype-v1.0.0           # Contains a web app trained using Teachable Machine.
    │   ├── 2-desktop-based-prototype-v1.0.0       # Contains py apps basic prototypes.
    ├── source                                 # Contains main source code.
    │   ├── 0-robot-resetter.py                    # Reset robot to default position.
    │   ├── 1-pose-based-main.py                   # Pose-based version.
    │   ├── 2-voice-based-main-english-version     # Voice-based English version.
    │   ├── 3-voice-based-main-tamil-version       # voice-based Tamil version.
    └── README.MD                              # Readme Content.

```

## 01 Introduction

This humanoid robot, powered by Arduino and AI, boasts impressive capabilities. It can interpret human poses, mimic arm movements, and respond to voice commands in both Tamil and English. Additionally, it can articulate its arms and head in response to voice inputs, making it versatile and interactive in multilingual environments. This dual-language functionality enhances its usability and appeal across diverse user bases.

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

To upload Firmata, open Arduino IDE and choose the correct COM port and **File -> Examples -> Firmata -> StandardFirmata -> Upload to Arduino UNO Board**.

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

- **Step 04 (Anaconda Env):** If you're using Anaconda, you can set up an environment that includes all the necessary dependencies.

  ```
   conda env create -f environment.yml
  ```

## 04 Usage

We have four Python programs:

- **Robot Resetter:** This script resets the robot to its default position. After removing the robot's arms and head, running this script readjusts all motors to their correct positions. Then, you can manually position the arms downwards and align the head to look straight ahead for setup.

- **Pose-based:** This program utilizes OpenCV and MediaPipe to track and mimic the movement of a human arm.

- **Voice-based English:**  This program employs Speech Recognition technology to understand and execute instructions spoken in the English language.

- **Voice-based Tamil:** This program utilizes Speech Recognition technology to comprehend and execute instructions spoken in the Tamil language.

- **Source Directory:**

  ```
  mr-humanoid\source

      * 0-robot-resetter.py
      * 1-pose-based-main.py
      * 2-voice-based-main-english-version.py
      * 3-voice-based-main-tamil-version.py

  ```

### 4.1 Setps to run

- **Step 01:** Connect the Arduino to the development computer.

- **Step 02:** Modify the script to reflect the appropriate COM port.

  ![Change COM Port](docs/media/2-change-com-port.png)


- **Step 03:** To reset the robot.

  ```
  python 0-robot-resetter.py
  ```

- **Step 04:** To run the Pose-based app.

  ```
  python 1-pose-based-main.py
  ```

- **Step 05:** To run the voice-based English version app.

  ```
  python 2-voice-based-main-english-version.py
  ```

- **Step 06:** To run the voice-based Tamil version app.

  ```
  python 3-voice-based-main-tamil-version.py
  ```

### 4.2 Output

<img src="docs/media/4-output-pose-1.gif" alt="Output Pose 1" width="100%">

![Output Pose 2](docs/media/5-output-pose-2.jpg)

![Output Pose 3](docs/media/6-output-pose-3.jpg)

![Output Voice 1](docs/media/7-output-voice.jpg)


# 05 Documentation

## 5.1 Voice Commands English

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


## 5.1 Voice Commands Tamil

| Voice Commands                           |
| ---------------------------------------- |
| **வலது கையை தூக்கவும்**                  |
| **வலது கையை மேல் நோக்கி உயர்த்தவும்**    |
| **வலது கையை மேல் நோக்கி தூக்கவும்**    |
| **வலது கையை உயர்த்தவும்**                 |
| **வலது கையை மேல் நோக்கி எழுப்பவும்**     |
| **வலது பக்க கையை உயர்த்தவும்**             |
| **கையை உயர்த்தவும்**                       |
| **வலது பக்க கையை மேல் நோக்கி உயர்த்தவும்** |
| **இடது கையை தூக்கவும்**                  |
| **இடது கையை மேல் நோக்கி உயர்த்தவும்**    |
| **இடது கையை மேல் நோக்கி தூக்கவும்**    |
| **இடது கையை உயர்த்தவும்**                 |
| **இடது கையை மேல் நோக்கி எழுப்பவும்**     |
| **இடது பக்க கையை உயர்த்தவும்**             |
| **இடது பக்க கையை உயர்த்தவும்**              |
| **இடது பக்க கையை மேல் நோக்கி உயர்த்தவும்** |
| **வலது கையை கீழே இரக்கவும்**               |
| **வலது கையை கீழ் நோக்கி இரக்கவும்**       |
| **வலது கையை கீழே விடவும்**                 |
| **வலது கையை கீழே பதிக்கவும்**              |
| **வலது கையை கீழ் நோக்கி விடவும்**         |
| **வலது பக்க கையை பதிக்கவும்**              |
| **வலது பக்க கையை கீழ் நோக்கி இரக்கவும்**  |
| **வலது பக்க கையை இரக்கவும்**               |
| **இடது கையை கீழே இரக்கவும்**               |
| **இடது கையை கீழ் நோக்கி இரக்கவும்**       |
| **இடது கையை கீழே விடவும்**                 |
| **இடது கையை கீழே பதிக்கவும்**              |
| **இடது கையை கீழ் நோக்கி விடவும்**         |
| **இடது பக்க கையை பதிக்கவும்**              |
| **இடது பக்க கையை பதிக்கவும்**               |
| **இடது பக்க கையை கீழ் நோக்கி இரக்கவும்**  |
| **நேரே பார்க்கவும்**                       |
| **முன் நோக்கி பார்க்கவும்**                 |
| **தலையை முன் நோக்கி பார்க்கவும்**         |
| **தலையை முன் பக்கம் வைக்கவும்**           |



# Contact

### 🌐 Website:
[![Visit](https://img.shields.io/badge/Visit%3A%20www.mpowerr.com-%23007ACC?style=flat&logo=google-chrome&logoColor=white&labelWidth=200)](https://www.mpowerr.com)

---

### 📱 Social Media:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/mpowerr-info)
[![Facebook](https://img.shields.io/badge/Facebook-%231877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/mpowerr.info)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/mpowerr.info)
[![X (Twitter)](https://img.shields.io/badge/X-%231DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/MpowerrInfo)
[![TikTok](https://img.shields.io/badge/TikTok-%23000000?style=for-the-badge&logo=tiktok&logoColor=white)](https://www.tiktok.com/@mpowerr.info)
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@mpowerrinfo)

---
