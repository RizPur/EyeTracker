# EyeTracker System 🧑‍💻

## Description 📝

The EyeTracker system is an assistive technology that enables users to type with their eyes 👀. By leveraging a USB webcam and a simple button interface, the system detects the position of the user's pupils and maps them onto a virtual keyboard on the screen. This innovative approach allows for typing without the need for traditional input devices and includes text-to-speech functionality to vocalize the typed words 🗣️.

## Key Components 🔑

The repository includes several essential files that contribute to the EyeTracker's functionality:

- `Static/`: Contains CSS and JavaScript files, crucial for the main script's operation, including modules like jQuery.
- `Templates/index1.html`: Hosts the keyboard interface and server-side JavaScript code.
- `eyes.py`: The primary image processing script for pupil tracking.
- `flaskbog.py`: The Flask application that launches the web interface.
- `ArduinoFinalYP.c`: Manages button and gyroscopic input.

Other files in the repository are for testing or support the main scripts indirectly.

## Installation and Execution 🚀

To get the EyeTracker system up and running:

1. Connect a USB webcam and the button circuit to your computer.
2. Run the `flaskbog.py` script to start the web application.

## Configuration Notes ⚙️

- Adjust the eye detection sensitivity in `eyes.py` (threshold range: 0 - 255, set at line 6).
- Modify the visible box limit in the video feed within `eyes.py` (lines 121 - 124).
- Change the communication port settings in `flaskbog.py`.
- Tweak the error values for eye coordinate mapping in `Templates/index1.html` (lines 427-428).

## Documentation 📚

Explore the project's detailed explanation, including a report, poster, and PowerPoint presentation, at the [project documentation link](https://www.dropbox.com/sh/rxno9jgkgpzz1ou/AAB3DmIJprQ1kS404O4goReOa?dl=0).

## Future Enhancements 🌟

- **Infrared Camera Integration**: To boost accuracy and minimize pupil detection errors.
- **Y Coordinate Optimization**: Improving the selection process by:
  - Using eye movement to select between two columns on the keyboard.
  - Employing buttons to choose the desired column, then switching to row selection for letter choice.

---

Contributions and suggestions are welcome to help enhance the EyeTracker system. Thank you for your support and interest! 🙏
