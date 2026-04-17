import cv2
import pygame
from djitellopy import Tello
import time
import numpy as np


# Basic connection
tello = Tello()
tello.connect()
print("Battery:", tello.get_battery())
tello.streamon()
time.sleep(2)  # Wait for stream to be ready


def init():
    pygame.init()
    pygame.display.set_mode((360, 240))
    pygame.display.set_caption("Tello Control")


def getKeyboardInput(img, keys):
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 30

    if keys[pygame.K_LEFT]:   lr = -speed
    elif keys[pygame.K_RIGHT]: lr = speed

    if keys[pygame.K_UP]:   fb = speed
    elif keys[pygame.K_DOWN]: fb = -speed

    if keys[pygame.K_w]: ud = speed
    elif keys[pygame.K_s]: ud = -speed

    if keys[pygame.K_a]: yv = speed
    elif keys[pygame.K_d]: yv = -speed

    if keys[pygame.K_e]:
        tello.takeoff()
        time.sleep(0.2)
    if keys[pygame.K_q]:
        tello.land()

    if keys[pygame.K_z]:
        cv2.imwrite(f"Image_{time.time()}.jpg", img)
        time.sleep(0.1)

    return [lr, fb, ud, yv]


def main():
    frame_read = tello.get_frame_read()
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()

    while True:
        # --- Process ALL events once per frame ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tello.land()
                tello.streamoff()
                pygame.quit()
                return

        keys = pygame.key.get_pressed()

        # --- Get frame ---
        img = frame_read.frame
        if img is None:
            continue

        img = img.copy()
        img = cv2.resize(img, (360, 240))
        # cv2 gives BGR; convert to RGB only for pygame display
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # --- Keyboard input (pass raw BGR img for saving) ---
        vals = getKeyboardInput(img, keys)
        tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])

        # --- Render frame to pygame window ---
        surface = pygame.surfarray.make_surface(np.rot90(img_rgb))
        screen.blit(surface, (0, 0))
        pygame.display.update()

        clock.tick(30)  # Cap at 30 FPS, no blocking sleep needed


if __name__ == "__main__":
    init()
    main()
