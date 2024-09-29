import numpy as np
import sounddevice as sd

# Diccionario con las frecuencias de las notas de una octava
notas_frecuencias = {
    'A': 440.00,    # La
    'A#': 466.16,   # La#
    'B': 493.88,    # Si
    'C': 523.25,    # Do
    'C#': 554.37,   # Do#
    'D': 587.33,    # Re
    'D#': 622.25,   # Re#
    'E': 659.25,    # Mi
    'F': 698.46,    # Fa
    'F#': 739.99,   # Fa#
    'G': 783.99,    # Sol
    'G#': 830.61    # Sol#
}

# Función para generar y reproducir una nota musical
def reproducir_nota(frecuencia, duracion, volumen=0.5, tasa_muestreo=44100):
    """
    Genera y reproduce una nota musical con una frecuencia dada.
    
    frecuencia: Frecuencia de la nota en Hz.
    duracion: Duración de la nota en segundos.
    volumen: Volumen del sonido (entre 0.0 y 1.0).
    tasa_muestreo: Tasa de muestreo en Hz (normalmente 44100 Hz).
    """
    # Generar una onda sinusoidal
    t = np.linspace(0, duracion, int(tasa_muestreo * duracion), False)
    onda = volumen * np.sin(2 * np.pi * frecuencia * t)

    # Reproducir la onda sonora
    sd.play(onda, tasa_muestreo)

    # Esperar a que el sonido termine antes de continuar
    sd.wait()

# Función para reproducir todas las notas de una octava
def reproducir_octava(duracion=1):
    """
    Reproduce una octava completa (A, A#, B, C, C#, D, D#, E, F, F#, G, G#).
    
    duracion: Duración de cada nota en segundos.
    """
    for nota, frecuencia in notas_frecuencias.items():
        print(f"Reproduciendo {nota} - {frecuencia} Hz")
        reproducir_nota(frecuencia, duracion)

# Reproducir una octava completa
reproducir_octava(duracion=0.75)  # Cada nota suena por 0.75 segundos
