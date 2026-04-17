import pygame

# Press key using PyGame to test keyboard input
def init():
    pygame.init()
    window = pygame.display.set_mode((400, 400))

def getKey(keyName):
    ans = False

    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, "K_{}".format(keyName)) #To have a format of K_{LEFT, RIGHT, UP, DOWN}
    print('K_{}'.format(keyName))
    
    if keyInput[myKey]:
        ans = True
    
    pygame.display.update()
    return ans

def main():
    if getKey("LEFT"): print("Left key is pressed")

    if getKey("RIGHT"): print("Right key is pressed")

if __name__ == "__main__":
    init()
    while True:
        main()
        