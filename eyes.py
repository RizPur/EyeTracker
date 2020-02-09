import cv2 
import numpy as np
import base64

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
thresh = 11
def imagejson(image):
    _, buffer = cv2.imencode('.jpg', image)
    eyejpg = base64.b64encode(buffer)
    #print(eyejpg)
    return eyejpg

def blurjson(image):
    blur_eye = blob_process(image, thresh, detector)
    _, buffer1 = cv2.imencode('.jpg', blur_eye)
    blurjpg = base64.b64encode(buffer1)
    print(buffer1)
    return blurjpg


def readB64(uri):
   encoded_data = uri.split(',')[1]
   nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
   img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
   return img



def resize(frame, scale):
    #print("Original Dimensions: ",frame.shape) # https://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python
    wideScale = int(frame.shape[1] * scale)
    heightScale = int(frame.shape[0] * scale)
    newDimensions = (wideScale, heightScale)
    frame = cv2.resize(frame, newDimensions, interpolation = cv2.INTER_AREA)
    #print("New Dimensions: ", frame.shape)
    return frame

def theBiggest(eyes):
    if len(eyes) > 1:
        biggest = (0,0,0,0)
        for i in eyes:
            if i[3] >= biggest[3]:
                biggest = i
        biggest = np.array([i], np.int32)
    elif len(eyes) == 1:
        biggest = eyes
    else:
        biggest = (0, 0, 0, 0)  
    return biggest

def theEye(biggest, frame, eye):
    for (ex,ey,ew,eh) in biggest: 
        #print(biggest)
        if eh < 200:
            biggest = last_biggest
        eye = frame[ey:ey+eh, ex:ex+ew]
        eyeCenter = ex + ew/2 
        cv2.rectangle(frame, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2) # draw rectange around it
        eh_l, ew_l = eye.shape[:2]
        eyebrowh_l = int(eh_l/4) 
        eye = frame[45:227+45, 284:284+180]
        last_biggest = biggest
        print("Eyes:", biggest)
    return eye 

#blobs
def blob_process(img, threshold, detector):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, img = cv2.threshold(gray_frame, threshold, 255, cv2.THRESH_BINARY_INV)
    img = cv2.erode(img, None, iterations=2)
    img = cv2.dilate(img, None, iterations=4)
    img = cv2.medianBlur(img, 5)
   # img = cv2.GaussianBlur(img, (7, 7), 0)
    keypoints = detector.detect(img)
    #print(keypoints)
    return img

detector_params = cv2.SimpleBlobDetector_Params()
detector_params.filterByArea = True
detector_params.maxArea = 1500 # no pupil can be larger than 1500p
detector = cv2.SimpleBlobDetector_create(detector_params)

#/blobs

def pupil(contours, eye):
    for cnt in contours:

        cv2.drawContours(eye, [cnt], -1, (0, 0, 255), 2)
        (x, y, w, h) = cv2.boundingRect(cnt)
        xPupil = int(x+w/2)
        yPupil = int(y+h/2)
        print('Pupil Center: ', xPupil, yPupil)
        #cv2.rectangle(eye, (x,y), (x+w, y+h), (255, 0, 0), 1)
        cv2.line(eye, (xPupil,0), (xPupil, 300), (200,0,0), 1 )
        cv2.line(eye, (0, yPupil), (400, yPupil), (200, 0, 0), 1)
        break
    return imagejson(eye)



#cap = cv2.VideoCapture("eyevid4.mp4")
last_biggest = (0, 0, 0, 0)


def getXY(frames):

    if frames is None:
        print("No frames detected")
        return -1
    frame = resize(frames, 1)

    
    eyes = eye_cascade.detectMultiScale(frame) #array of arrays of eyes
   # print(eyes)
    #biggest = theBiggest(eyes) #find a way to stop crashing when biggest not detected    
    #eye = theEye(biggest, frame, eye)
    #eye = frame[45:227+45, 260:284+190] #eyevid2
    #eye = frame[52:52+269, 356:352+356] #eyevid3
    #eye = frame[140:52+260, 200:200+200] #eyevid4
    eye = frame
    gray_eye = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)

    blur_eye = blob_process(eye, thresh, detector)
    _, contours, _ = cv2.findContours(blur_eye, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse = True) #sorts from biggest 
    #print(contours)
    xPupil = 0
    yPupil = 0
    for cnt in contours:

        cv2.drawContours(eye, [cnt], -1, (0, 0, 255), 2)
        (x, y, w, h) = cv2.boundingRect(cnt)
        xPupil = int(x+w/2)
        yPupil = int(y+h/2)
        #print('Pupil Center: ', xPupil, yPupil)
        #cv2.rectangle(eye, (x,y), (x+w, y+h), (255, 0, 0), 1)
        cv2.line(eye, (xPupil,0), (xPupil, 300), (200,0,0), 1 )
        cv2.line(eye, (0, yPupil), (400, yPupil), (200, 0, 0), 1)
        break
    
    

    # cv2.imshow('Gray eye', eye)
    # cv2.imshow("Blur", blur_eye)

    # key = cv2.waitKey(1)
    # if key == 27:
    #   cv2.destroyAllWindows()

    return xPupil, yPupil

def test(frames):
    cv2.imshow("Test", frames)
    key = cv2.waitKey(1)
    if key == 27:
        cv2.destroyAllWindows()



#call a script from a script
#https://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-script-from-another-script