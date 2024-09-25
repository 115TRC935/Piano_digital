import cv2
import numpy as np

# Cargar las plantillas de símbolos
templates = [
    ('A', cv2.imread('A.png', 0)),
    ('A#', cv2.imread('A#.png', 0)),
    ('B', cv2.imread('B.png', 0)),
    ('C', cv2.imread('C.png', 0)),
    ('C#', cv2.imread('C#.png', 0)),
    ('D', cv2.imread('D.png', 0)),
    ('D#', cv2.imread('D#.png', 0)),
    ('E', cv2.imread('E.png', 0)),
    ('F', cv2.imread('F.png', 0)),
    ('F#', cv2.imread('F#.png', 0)),
    ('G', cv2.imread('G.png', 0)),
    ('G#', cv2.imread('G#.png', 0)),
]

# Cargar la imagen de prueba
img = cv2.imread('prueba4.png', 0)

# Variables para almacenar el mejor símbolo encontrado
best_match = None
best_val = float('inf')

# Comparar la imagen con cada plantilla
for label, template in templates:
    res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF)
    min_val, _, min_loc, _ = cv2.minMaxLoc(res)

    # Buscar la mejor coincidencia
    if min_val < best_val:
        best_val = min_val
        best_match = label

# Imprimir el resultado
if best_match is not None:
    print(f'Símbolo detectado: {best_match}')
else:
    print('No se detectó ningún símbolo.')
