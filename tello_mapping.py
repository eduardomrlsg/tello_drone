import cv2
from djitellopy import Tello
import numpy as np
import KeyPressModule as kp
import time

# Parameters (Test it for your drone and adjust accordingly)
fSpeed = 117 / 10  # Forward Speed in cm/s (15cm/s)
aSpeed = 360 / 10  # Angular Speed in degrees/s
interval = 0.25  # Time interval for mapping positions in seconds

dInterval = fSpeed * interval  # Distance interval in cm
aInterval = aSpeed * interval  # Angle interval in degrees


class FakeTello:
    def connect(self):
        print("Fake drone connected")

    def get_battery(self):
        return 100

    def send_rc_control(self, lr, fb, ud, yv):
        print(f"RC -> lr:{lr}, fb:{fb}, ud:{ud}, yv:{yv}")

    def takeoff(self):
        print("Takeoff")

    def land(self):
        print("Land")

kp.init()
tello = FakeTello()
#tello = Tello()
tello.connect()
print("Battery:", tello.get_battery())
x, y = 500, 500
a = 0
yaw = 0 
points = []


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 15
    d = 0 
    global x, y, yaw, a

    if kp.getKey("LEFT"): 
        lr = -speed 
        d = dInterval
        a = -180 

    elif kp.getKey("RIGHT"): 
        lr = speed
        d = -dInterval
        a = 180 

    if kp.getKey("UP"): 
        fb = speed
        d = dInterval
        a = 270

    elif kp.getKey("DOWN"): 
        fb = -speed
        d = -dInterval
        a = -90

    if kp.getKey("w"): 
        ud = speed
    elif kp.getKey("s"): 
        ud = -speed

    if kp.getKey("a"): 
        yv = speed
        yaw += aInterval

    elif kp.getKey("d"): 
        yv = -speed
        yaw -= aInterval

    if kp.getKey("q"): tello.land(); time.sleep(3) 
    if kp.getKey("e"): tello.takeoff()

    time.sleep(interval)
    a += yaw
    x += int(d * np.cos(np.radians(a)))
    y += int(d * np.sin(np.radians(a)))



    return [lr, fb, ud, yv, x, y]

def drawPoints(img, points):
    cv2.circle(img, (points[0], points[1]), 5, (0, 0, 255), cv2.FILLED)


while True:
    vals = getKeyboardInput()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    
    img = np.zeros((1000, 1000, 3), np.uint8)
    points.append((vals[4], vals[5]))
    drawPoints(img, points)
    cv2.imshow("Output", img)
    cv2.waitKey(1)
