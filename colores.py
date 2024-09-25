import cv2
import numpy as np

# Cargar la imagen

def plantillas():
  print("plantillas")
  templates = [
      # cv2.imread('A.png'),cv2.imread('A#.png')
       cv2.imread('images\A.png'), #'A'
       cv2.imread('images\A#.png'), #'A#'
       cv2.imread('images\B.png'), #'B'
       cv2.imread('images\C.png'), #'C'
       cv2.imread('images\C#.png'), #'C#'
       cv2.imread('images\D.png'), #'D'
       cv2.imread('images\D#.png'), #'D#'
       cv2.imread('images\E.png'), #'E'
       cv2.imread('images\F.png'), #'F'
       cv2.imread('images\F#.png'), #'F#'
       cv2.imread('images\G.png'), #'G'
       cv2.imread('images\G#.png'), #'G#'
  ]

  gray=[]
  resized_img=[]
  norm_img=[]
  binarized_img=[]
  for i in range (0,len(templates)):
    # Convertir a escala de grises
    gray.append(cv2.cvtColor(templates[i], cv2.COLOR_BGR2GRAY))
    # Redimensionar la imagen a 3x3 píxeles
    resized_img.append(cv2.resize(gray[i], (3, 3), interpolation=cv2.INTER_AREA))
    # Normalizar los valores para obtener una matriz entre 0 y 1 (opcional)
    norm_img.append(resized_img[i] / 255.0)
    _, binarized_img_i = cv2.threshold(resized_img[i], 127, 1, cv2.THRESH_BINARY)
    binarized_img.append(binarized_img_i)

  # print("Matriz 3x3:")
  # for i in range (0,len(templates)):
  #   print(norm_img[i],"\n")

  print("Matriz binaria 3x3:")
  for i in range (0,len(templates)):
    print(binarized_img[i],"\n")
  return(binarized_img)

def reconocimientoTest():
  print("reconocimientoTest")
  # Cargar la imagen
  img = cv2.imread('images\prueba5.png')
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  rezized_img = cv2.resize(gray, (3, 3), interpolation=cv2.INTER_AREA)
  norm_img = rezized_img / 255.0
  _, binarized_img = cv2.threshold(rezized_img, 127, 1, cv2.THRESH_BINARY)

  # print("Matriz 3x3:")
  # print(norm_img)
  print("Matriz binaria 3x3:")
  print(binarized_img)
  return(binarized_img)

def comparar():
  print("comparar")
  # Comparar la imagen con cada plantilla
  best_match = None
  val=reconocimientoTest()
  for i, template in enumerate(plantillas()):
    if np.array_equal(val, template):
      best_match = i
      break
  # for each in plantillas():
  #   if (reconocimiento()== each):
  #     best_match = plantillas().index(each)


  # Imprimir el resultado
  if best_match is not None:
    print(f'Símbolo detectado: {["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"][best_match]}')
  else:
    print('Ninguna coincide.')
def main():
  comparar()

if __name__ == "__main__":
    main()
