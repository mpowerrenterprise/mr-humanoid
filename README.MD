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

## 02 Technology Stack

### 2.1 Hardware Stack

- Arduino UNO (1)
- 180deg Micro Servo Motor (3)
- Full / Half Bread Board (1)
- Jumper Wires

### 2.2 Software Stack

- Python 3.8.5
- Arduino IDE (Framework)
- OpenCV pyfirmata
- Mediapipe 0.10.3
- PyFirmata
- SpeechRecognition
- PyAudio

## 3.0 Setup

## 3.1 Hardware Setup

![Circuit Diagram](docs/media/0-circuit-diagram.png)

| Objects       | Pin No  |
| ------------- | ------- |
| **Left Arm**  | Pin: 13 |
| **Right Arm** | Pin: 12 |
| **Head**      | Pin: 11 |

## 3.2 Firmware Setup

It is necessary to set up the Arduino firmware to enable communication between Python and Arduino. The Firmata protocol establishes serial communication between a Python script and an Arduino.

To upload Firmata, open Arduino IDE and choose the correct COM port and **file -> Examples -> Firmata -> StandardFirmata -> Upload to Arduino UNO Board**.

![Firmware Setup](docs/media/1-firmware-setup.png)
