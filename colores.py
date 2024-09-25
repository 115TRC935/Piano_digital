import cv2
import numpy as np

# Cargar la imagen
img = cv2.imread('prueba2.png')

# Convertir a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Redimensionar la imagen a 3x3 píxeles
resized_img = cv2.resize(gray, (3, 3), interpolation=cv2.INTER_AREA)

# Normalizar los valores para obtener una matriz entre 0 y 1 (opcional)
norm_img = resized_img / 255.0

# Imprimir la matriz resultante
print("Matriz 3x3:")
print(norm_img)

# Si prefieres la matriz en formato binario (0 y 1) en lugar de valores de escala de grises:
_, binarized_img = cv2.threshold(resized_img, 127, 1, cv2.THRESH_BINARY)
print("Matriz binaria 3x3:")
print(binarized_img)
