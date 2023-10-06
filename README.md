# Python Virtual Mouse - Eye and Hand Tracking

This project enables mouse control using eye and hand tracking. With two separate Python scripts, you can navigate your computer screen effortlessly. The "Eye Control" script tracks your eye movements to control the mouse, while the "Hand Control" script uses hand gestures to manipulate the cursor. This versatile project offers a unique way to interact with your computer.

![Virtual Mouse](https://drive.google.com/uc?id=1qjZksEVllcyT8enchl1OCkFWhQMZVoJC)


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## Introduction

The Python Mouse Control project provides two distinct methods for navigating your computer screen. The "Eye Control" script utilizes eye tracking to move the cursor, and the "Hand Control" script employs hand gestures for cursor manipulation. Whether you prefer precise eye movements or intuitive hand gestures, this project offers an alternative way to interact with your computer.

## Features

### Eye Control
- Track eye movements to control the mouse cursor.
- Click the mouse by blinking your eyes (requires calibration).
- Smooth and precise cursor movement.

### Hand Control
- Use hand gestures to control the cursor.
- Click the mouse by touching the thumb and index finger.
- Efficient and intuitive control.

## Getting Started

To get started with this project, follow these steps:

### Prerequisites

- Python installed on your system.
- Required Python libraries: OpenCV, Mediapipe, and PyAutoGUI.
- A webcam for tracking.

### Installation

### 1. Get Source Code Files
#### Option 1: Clone Repository

- If you have Git installed, you can clone the repository using the following command:

  ```bash
  git clone https://github.com/VineetKumar02/Virtual-Mouse.git
  ```

- After cloning, navigate to the project directory:

  ```bash
  cd Virtual-Mouse
  ```

#### Option 2: Download ZIP

- If you prefer not to use Git, you can download the ZIP archive of the project:

  1. Click the "Code" button on the repository page.
  2. Choose "Download ZIP."
  3. Extract the downloaded ZIP file to a location of your choice.

### 2. Install Dependencies

Install the required Python libraries using pip:

1. Using Reqirements.txt file
    ```bash
    pip install -r requirements.txt
    ```

    or

2. For latest version of packages (May not work. If fails.. Follow method 1)

    ```bash
    pip install opencv-python mediapipe pyautogui
    ```

## Usage

1. **Eye Control:**

   - Run the "eye_mouse.py" script:

     ```bash
     python eye_mouse.py
     ```

   - Calibrate the eye tracking by following the on-screen instructions.
   - Control the mouse cursor with your eye movements.
   - Blink to click the mouse.

2. **Hand Control:**

   - Run the "hand_mouse.py" script:

     ```bash
     python hand_mouse.py
     ```

   - Use hand gestures to move the cursor.
   - Touch your thumb and index finger to click the mouse.

## Technologies Used

- Python
- OpenCV
- Mediapipe
- PyAutoGUI

## Contributing

Contributions to this project are welcome. If you have any suggestions, enhancements, or bug fixes, please open an issue or submit a pull request.

---
**Note:** This project is for educational and demonstration purposes. It may require calibration for optimal performance, and results may vary based on lighting conditions and hardware capabilities.