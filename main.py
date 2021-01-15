import cv2
import numpy as np
from pyzbar.pyzbar import decode


#img = cv2.imread('Shantonu.png')
cap = cv2.VideoCapture(0)
cap.set(3,460)
cap.set(4,480)


with open('MyData.txt') as f:
    myDataList = f.read().splitlines()
#print(myDataList)


while True:
    success,img = cap.read()
    for barcode in decode(img):
        #print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myDataList:
            myOutput = 'Authorized'
            myColor = (0,255,0)
            print('Authorized')
            welcome = 'WELCOME SIR'
            index = (240,420)

        else:
