from wsgiref.simple_server import WSGIRequestHandler
import cv2
import numpy as np
from time import sleep

vid = cv2.VideoCapture(0)
prevColor = ''

# Initial read to calibrate default view
input("Press enter to calibrate default color profile.")
_, frame = vid.read()
b = frame[:, :, :1]
g = frame[:, :, 1:2]
r = frame[:, :, 2:]

b_def = np.mean(b)
g_def = np.mean(g)
r_def = np.mean(r)

try:
    while True:

        _, frame = vid.read()
        cv2.imshow("frame", frame)
        cv2.waitKey(100)

        b = frame[:, :, :1]
        g = frame[:, :, 1:2]
        r = frame[:, :, 2:]

        b_mean = np.mean(b)
        g_mean = np.mean(g)
        r_mean = np.mean(r)

        #print("R:",r_mean,"G:",g_mean,"B:",b_mean)
        print(b_mean > g_mean and b_mean > r_mean)

        if b_mean > g_mean and b_mean > r_mean and prevColor != 'b':
            print("Blue")
            sleep(1)
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
