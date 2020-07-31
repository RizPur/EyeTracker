*Description*

This system maps the position of the pupil onto a letter box on the screen enabling users to type with their eyes and two buttons.
The words can be then spoken aloud.

There are several files in this repository that do not coontribute to the working eyetracker keyboard code. 
The necessary files are:

Static -> CSS  and jS (this jS files holds necessary modules for main script to work such as jQuery)

Templates -> index1.html (holds the main keyboard and server html and jS code)

eyes.py (this is main image processing script)

flaskbog.py (this is flask application that launches the website)

ArduinoFinalYP.c (button/gyro code)

The other files are either used for tests or are used in the background by the main scripts

*HOW TO RUN*

Connect the button circuit to the computer using the programmer and run the flaskbog.py script

*NOTE*

The colour threshold for the eye recording is located in the eyes.py (thresh 0 - 255 [line 6]) increase or decrease until only pupil blob is visible. 
The box limit seen on video can be changed in eyes.py (line 121 - 124).
The com port can be changed in the flaskbog.py script.
The error values for the eye coordinates can be changed in index1.html (line 427-428).

Read the report, poster and PowerPoint presentation here: 
https://www.dropbox.com/sh/rxno9jgkgpzz1ou/AAB3DmIJprQ1kS404O4goReOa?dl=0

