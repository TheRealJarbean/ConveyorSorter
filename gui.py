from cProfile import run
from threading import Thread
from time import sleep
import tkinter as tk
from wsgiref.simple_server import WSGIRequestHandler
import cv2
import numpy as np

red_enabled = True
green_enabled = True
blue_enabled = True

def run_gui():
    window = tk.Tk()

    def en_red():
        global red_enabled
        enbuttons[0]["state"] = "disabled"
        disbuttons[0]["state"] = "active"
        red_enabled = True

    def en_green():
        global green_enabled
        enbuttons[1]["state"] = "disabled"
        disbuttons[1]["state"] = "active"
        green_enabled = True

    def en_blue():
        global blue_enabled
        enbuttons[2]["state"] = "disabled"
        disbuttons[2]["state"] = "active"
        blue_enabled = True

    def dis_red():
        global red_enabled
        disbuttons[0]["state"] = "disabled"
        enbuttons[0]["state"] = "active"
        red_enabled = False

    def dis_green():
        global green_enabled
        disbuttons[1]["state"] = "disabled"
        enbuttons[1]["state"] = "active"
        green_enabled = False

    def dis_blue():
        global blue_enabled
        disbuttons[2]["state"] = "disabled"
        enbuttons[2]["state"] = "active"
        blue_enabled = False

    # Create primary panes
    frm_leftpane = tk.Frame(master = window, width = 500, height = 220, pady = 5)
    frm_rightpane = tk.Frame(master = window)

    # Pack primary panes
    frm_leftpane.pack(side = tk.LEFT)
    frm_rightpane.pack(side = tk.RIGHT)

    # Create and pack left pane content
    lbl_currentColor = tk.Label(master = frm_leftpane, text = "Blue")
    lbl_currentColor.pack()
    frm_currentColor = tk.Frame(master = frm_leftpane, background = "blue", width = 100, height = 100)
    frm_currentColor.pack(fill = "both", padx = 20, pady = 20)

    # Create and pack enable buttons
    enbuttons = [
        tk.Button(master = frm_rightpane, text = "Accept", relief = tk.RAISED, width = 12, height = 4, state = "disabled", command = en_red),
        tk.Button(master = frm_rightpane, text = "Accept", relief = tk.RAISED, width = 12, height = 4, state = "disabled", command = en_green),
        tk.Button(master = frm_rightpane, text = "Accept", relief = tk.RAISED, width = 12, height = 4, state = "disabled", command = en_blue)
    ]

    i = 0
    for btn in enbuttons:
        btn.grid(row = 0, column = i)
        i += 1

    # Create and pack color labels
    i = 0
    for color in [ "red", "green", "blue"]:
        tk.Frame(master = frm_rightpane, background = color, width = 95, height = 95).grid(row = 1, column = i)
        i += 1

    # Create and pack disable buttons
    disbuttons = [
        tk.Button(master = frm_rightpane, text = "Reject", relief = tk.RAISED, width = 12, height = 4, command = dis_red),
        tk.Button(master = frm_rightpane, text = "Reject", relief = tk.RAISED, width = 12, height = 4, command = dis_green),
        tk.Button(master = frm_rightpane, text = "Reject", relief = tk.RAISED, width = 12, height = 4, command = dis_blue)
    ]

    i = 0
    for btn in disbuttons:
        btn.grid(row = 2, column = i)
        i += 1

    window.mainloop()
    
def run_testprint():
    global red_enabled
    global green_enabled
    global blue_enabled

    print(red_enabled, green_enabled, blue_enabled)
    sleep(1)

# Start GUI thread
Thread(target=run_gui).start()

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