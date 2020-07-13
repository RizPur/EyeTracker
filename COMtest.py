import serial

def transmit(index):
	return numArr[index]

#socketio.emit("response", {'x': x, 'y': y, 'img': eyes.imagejson(frames), 'blur': eyes.blurjson(frames), 'btn1': COMtest.transmit(0), 'btn2': COMtest.transmit(1), 'gyroX': COMtest.transmit(2), 'gyroY': COMtest.transmit(3), 'gyroZ': COMtest.transmit(4) })

arduino = serial.Serial('COM6', 9600, timeout=.1)

while True:
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		#print("ready")
		arr = data.decode('utf-8').split(',')
		numArr = list(map(int, arr))
		print(data)

		
        