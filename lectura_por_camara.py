import cv2
import numpy as np

def create_symbol_dict(image_path):
    # Leer la imagen
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Binarizar la imagen
    _, binary = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
    
    # Encontrar contornos
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    symbols = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        symbol = binary[y:y+h, x:x+w]
        symbols.append(symbol)
    
    # Crear diccionario de símbolos
    symbol_dict = {}
    for i, symbol in enumerate(symbols):
        symbol_dict[i] = cv2.resize(symbol, (50, 50))  # Redimensionar para consistencia
    
    return symbol_dict

def match_symbol(frame, symbol_dict):
    # Preprocesar el frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    
    # Encontrar contornos
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Tomar el contorno más grande
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        
        # Extraer el símbolo
        symbol = binary[y:y+h, x:x+w]
        
        # Redimensionar para comparar
        symbol = cv2.resize(symbol, (50, 50))
        
        # Comparar con los símbolos del diccionario
        best_match = None
        best_score = float('inf')
        
        for index, dict_symbol in symbol_dict.items():
            score = np.sum(np.abs(symbol.astype(int) - dict_symbol.astype(int)))
            
            if score < best_score:
                best_score = score
                best_match = index
        
        return best_match
    
    return None

# Crear el diccionario de símbolos
image_path = 'simbolos.png'  # Reemplaza esto con la ruta real de tu imagen
symbol_dict = create_symbol_dict(image_path)

# Iniciar la captura de video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Voltear el frame horizontalmente para efecto espejo
    frame = cv2.flip(frame, 1)
    
    # Encontrar el símbolo en el frame
    matched_index = match_symbol(frame, symbol_dict)
    
    # Mostrar el resultado
    if matched_index is not None:
        cv2.putText(frame, f"Indice: {matched_index}", (50, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('Reconocimiento de Simbolos', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()