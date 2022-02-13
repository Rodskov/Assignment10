from unicodedata import name
import cv2
import numpy as np
from pyzbar.pyzbar import decode

#Write into .txt files
def writeFile():
    name = results[0].split()
    output = open(name + ".txt", 'w')
    output.write(results)
    output.close()

vidCam = cv2.VideoCapture(0)
vidCam.set(3, 640)
#vidCam.set(4, 480)

while True:
    ret, frame = vidCam.read()
    for qrcode in decode(frame):
        data = qrcode.data.decode('utf-8')
        results = data.split(",")
        print(data)
        #writeFile()
        point = np.array([qrcode.polygon], np.int32).reshape((-1, 1, 2))
        cv2.polylines(frame, [point], True, (230,230,250), 5)

    cv2.imshow("QR Scanner", frame)
    cv2.waitKey(1)
    #Press (Q) button to exit camera
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vidCam.release()
cv2.destroyAllWindows()