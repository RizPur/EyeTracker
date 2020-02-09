import eyes
from flask import Flask, render_template, url_for
from flask_socketio import SocketIO
import cv2 
import base64
from PIL import Image
from io import StringIO
import numpy as np
import logging







app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True
socketio = SocketIO(app)

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
    socketio.emit("response", {'x': x, 'y': y, 'img': eyes.imagejson(frames), 'blur': eyes.blurjson(frames) })

@app.route("/")
@app.route("/home")
def home():
    print("Helllo")
    return render_template('index1.html', x = 135, y = 122)


@app.route("/about")
def about():
    return render_template('about.html', title='made by Joel Brown')


if __name__ == '__main__':
    app.run(debug=True, port=5000)