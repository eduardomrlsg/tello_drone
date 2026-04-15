import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()

print("Battery:", tello.get_battery())

tello.streamon()

frame_read = tello.get_frame_read()
frames = 0

while True:
    frame = frame_read.frame

    # Convertir a gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Binarizar
    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    # Mostrar imágenes
    cv2.imshow("Original", frame)
    cv2.imshow("Binary", binary)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

tello.streamoff()
cv2.destroyAllWindows()


