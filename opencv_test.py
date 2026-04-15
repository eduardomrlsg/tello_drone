import cv2
import numpy as np

# Crear imagen de 400x400 con fondo azul oscuro
img = np.zeros((400, 400, 3), dtype=np.uint8)
img[:] = (50, 20, 10)  # BGR: azul oscuro

# Dibujar círculo rojo
cv2.circle(img, (200, 200), 100, (0, 0, 220), -1)

# Dibujar rectángulo verde
cv2.rectangle(img, (50, 50), (150, 150), (0, 200, 0), 3)

# Dibujar línea amarilla
cv2.line(img, (0, 400), (400, 0), (0, 220, 220), 2)

# Texto
cv2.putText(img, "OpenCV OK!", (90, 320),
            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2)

# Mostrar ventana
cv2.imshow("Test OpenCV", img)
print("OpenCV version:", cv2.__version__)
print("Presiona cualquier tecla para cerrar...")
cv2.waitKey(0)
cv2.destroyAllWindows()