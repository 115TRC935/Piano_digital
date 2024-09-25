import cv2
import numpy as np

# Leer la imagen
img = cv2.imread('image.png')

# Convertir a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar suavizado para eliminar ruido
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Aplicar umbral adaptativo para binarizar la imagen
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                               cv2.THRESH_BINARY_INV, 11, 2)

# Encontrar los contornos
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos en la imagen original
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Mostrar la imagen con los contornos detectados
cv2.imshow('Piano Teclas', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
