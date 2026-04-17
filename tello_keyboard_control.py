import cv2
import pygame
from djitellopy import Tello
from time import sleep

# Basic connection and takeoff test
tello = Tello()
tello.connect()
print("Battery:", tello.get_battery())


# Press key using PyGame to test keyboard input
def init():
    pygame.init()
    window = pygame.display.set_mode((400, 400))

def getKey(keyName):
    ans = False

    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, "K_{}".format(keyName)) #To have a format of K_{LEFT, RIGHT, UP, DOWN}
    if keyInput[myKey]:
        ans = True
        pygame.display.update()

    return ans

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 30
    if getKey("LEFT"): lr = -speed
    elif getKey("RIGHT"): lr = speed

    if getKey("UP"): fb = speed
    elif getKey("DOWN"): fb = -speed

    if getKey("w"): ud = speed
    elif getKey("s"): ud = -speed

    if getKey("a"): yv = speed
    elif getKey("d"): yv = -speed

    if getKey("q"): tello.land()
    if getKey("e"): tello.takeoff(); sleep(3) # Sleep to ensure the drone has time to take off before accepting new commands

    return [lr, fb, ud, yv]

def main():
    while True:
        vals = getKeyboardInput()
        tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
        sleep(0.05)

if __name__ == "__main__":
    init()
    while True:
        main()

    

