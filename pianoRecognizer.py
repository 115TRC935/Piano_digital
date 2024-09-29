import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('images/shapes.png')


# Convertir a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar umbral para convertir en imagen binaria
_, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Encontrar contornos en la imagen
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Iterar sobre los contornos encontrados
for contour in contours:
    # Aproximar el contorno a un polígono
    approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
    
    # Dibujar el contorno sobre la imagen original
    cv2.drawContours(image, [approx], 0, (0, 0, 0), 5)
    
    # Encontrar el centro del polígono
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    # Determinar el número de lados del polígono y etiquetar la forma

    match (len(approx)):
        case 3:
            cv2.putText(image, "Triangulo", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        case 4:
            cv2.putText(image, "Rectangulo", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        case 5:
            cv2.putText(image, "Pentagono", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        case 6:
            cv2.putText(image, "Hexagono", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        case _:
            cv2.putText(image, "Circulo", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
# Mostrar la imagen con las formas etiquetadas
cv2.imshow("Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
