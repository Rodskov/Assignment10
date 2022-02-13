import cv2
import numpy as np
from pyzbar.pyzbar import decode

#testEx = decode(cv2.imread("frame.png"))

vidCam = cv2.VideoCapture(0)
vidCam.set(3, 640)
vidCam.set(4, 480)

while True:
    success, img = vidCam.read()
    for qrcode in decode(img):
        results = qrcode.data.decode('utf-8')
        print(results)
    cv2.imshow("QR Scanner", img)
    cv2.waitKey(1)