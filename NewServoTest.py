from time import sleep
from gpiozero import Servo

servo = Servo(25)

while True:
    print("Working!")
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)
