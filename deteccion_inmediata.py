import cv2
import numpy as np
import mediapipe as mp
import sonidos  # Asumiendo que 'sonidos.py' contiene la función de reproducción de notas

# Inicializar mediapipe para detección de manos
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
#que ganas de ser profesor
# Función para capturar imagen del piano y detectar teclas
def detectar_teclas(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    
    # Detectar contornos
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    teclas = []

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
        if len(approx) == 4:  # Detectar contornos rectangulares (teclas)
            x, y, w, h = cv2.boundingRect(approx)
            teclas.append((x, y, w, h))
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame, teclas

# Función para verificar si un dedo toca una tecla
def detectar_toque(teclas, landmarks):
    for (x, y, w, h) in teclas:
        for lm in landmarks:
            if x < lm[0] < x + w and y < lm[1] < y + h:
                return (x, y, w, h)  # Retorna la tecla tocada
    return None

# Diccionario que mapea teclas a notas
teclas_a_notas = {
    0: 'A', 1: 'A#', 2: 'B', 3: 'C', 4: 'C#', 
    5: 'D', 6: 'D#', 7: 'E', 8: 'F', 9: 'F#', 
    10: 'G', 11: 'G#'
}

# Inicializar la cámara
cap = cv2.VideoCapture(0)
detectar_piano = True
teclas = []

# Iniciar detección de manos
with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Error al acceder a la cámara.")
            break
        
        # Etapa 1: Detección de teclas del piano
        if detectar_piano:
            frame, teclas = detectar_teclas(frame)
            cv2.putText(frame, "Presiona 'c' para confirmar ubicacion de teclas.", (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Confirmar ubicación de las teclas
        if cv2.waitKey(1) & 0xFF == ord('c'):
            detectar_piano = False  # Ya no necesitamos buscar teclas
        
        # Etapa 2: Detección de dedos y reproducción de sonidos
        if not detectar_piano and teclas:
            # Convertir la imagen a RGB para mediapipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_frame)
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    # Extraer posiciones de los dedos
                    landmarks = [(lm.x * frame.shape[1], lm.y * frame.shape[0]) 
                                 for lm in hand_landmarks.landmark]
                    
                    # Detectar si un dedo toca una tecla
                    tecla_tocada = detectar_toque(teclas, landmarks)
                    if tecla_tocada:
                        # Reproducir sonido de la tecla correspondiente
                        idx = teclas.index(tecla_tocada)
                        nota = teclas_a_notas.get(idx, "C")  # Asignar nota a la tecla
                        sonidos.reproducir_nota(nota, 1)  # Reproducir nota (duración 1s)
        
        # Mostrar el frame procesado
        cv2.imshow('Piano Digital', frame)

        # Salir con la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Liberar la cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows() 
