# Pomodoro Timer

A simple **Pomodoro Timer** built with **Python** and **Tkinter** that helps you stay productive by using the Pomodoro technique. The timer includes notifications to alert you when it's time to take breaks and when to resume working.

## Features

- **Pomodoro Technique**: Focus on work for 25 minutes and then take a 5-minute break. After four work sessions, take a longer break.
- **Customizable Time**: You can adjust the duration of work and break sessions.
- **Notifications**: Sends desktop notifications to remind you when a session ends and a break starts (requires a supported notification system).
- **User Interface**: Built using Tkinter for a simple and clean graphical interface.
- **Cross-platform**: Works on Windows, macOS, and Linux.

## Requirements

- **Python 3.x**
- **Tkinter** (usually included with Python installations)
- **plyer** (for notifications)

You can install `plyer` by running:

```bash
pip install plyer
```

## Project Structure
```bash
.
├── images
│   ├── icon.ico  # Icon for the notification
│   └── tomato.png  # Image for the UI
├── main.py  # Main script that runs the Pomodoro timer
├── README.md  # Project documentation
└── main.spec  # Spec file (if using pyinstaller)

```

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/JuanAlejandroCR/pomodoroPython
    ```

2. Navigate to the project directory:
    ```bash
    cd pomodoroPython
    ```

3. Install the required dependencies:
    ```bash
    pip install plyer
    ```

4. Run the Pomodoro timer:
    ```bash
    python3 main.py
    ```

## Customization
You can modify the duration of the work and break sessions by editing the respective constants in `main.py` :

```python
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
```


---