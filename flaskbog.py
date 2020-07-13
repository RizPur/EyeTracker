import eyes
#import COMtest
import serial
from flask import Flask, render_template, url_for
from flask_socketio import SocketIO
import cv2 
import base64
from PIL import Image
from io import StringIO
import numpy as np
import logging
from threading import Thread

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True
socketio = SocketIO(app)
thread = None
data = None

arduino = serial.Serial('COM6', 9600, timeout=.1)
print(cv2.__version__)

def background_thread():
    while True:
        global data
        data = arduino.readline() #gets rid of /r/n bits
        if data:
            data = data.decode("utf-8").split(',')
            print(data)
           # socketio.emit("dataReceived", {'data': data})



def transmit(index,numArr):
	return numArr[index]

@socketio.on("name")
def Event(data):
    print("Hello" + data)



@socketio.on("frame") #on the frame event
def show(image): 
    

    frames = eyes.readB64(image) 
    #cv2.imshow("Image", frames)
    #key = cv2.waitKey()
    x, y = eyes.getXY(frames)
    #eyes.test(frames)
    socketio.emit("response", {'x': x, 'y': y, 'img': eyes.imagejson(frames), 'blur': eyes.blurjson(frames), 'data': data})


@app.route("/")
@app.route("/home")
def home():
    print("Hi")
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.start()
    return render_template('index1.html', x = 135, y = 122)


@app.route("/about")
def about():
    return render_template('about.html', title='made by Joel Brown')


if __name__ == '__main__':
    app.run(debug=False, port=5000)