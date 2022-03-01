import cv2
import numpy as np
from gpiozero import Servo
from time import sleep

servo = Servo(25)
val = -1
servo.value = val

vid = cv2.VideoCapture(0)
prevColor = ''

try:
    while True:

        _, frame = vid.read()
        #cv2.imshow("frame", frame)
        #cv2.waitKey(100)

        b = frame[:, :, :1]
        g = frame[:, :, 1:2]
        r = frame[:, :, 2:]

        b_mean = np.mean(b)
        g_mean = np.mean(g)
        r_mean = np.mean(r)

        if b_mean > g_mean and b_mean > r_mean and prevColor != 'b':
            print("Blue")
            servo.value = servo.value + 1
            sleep(0.5)
            servo.value = servo.value - 1
            prevColor = 'b'
        elif g_mean > r_mean and g_mean > b_mean and prevColor != 'g':
            print("Green")
            prevColor = 'g'
        elif r_mean > g_mean and r_mean > b_mean and prevColor != 'r':
            print("Red")
            prevColor = 'r'

        sleep(0.25)

except KeyboardInterrupt:
    print("Program stopped.")
