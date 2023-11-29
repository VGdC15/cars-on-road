import pygame
import random
from vehiculo import Vehiculo
from constantesCar import *

# clase VehiculoEnemigo que hereda de la clase Vehiculo
class VehiculoEnemigo(Vehiculo):

    # Constructor de la clase, que llama al constructor de la clase base (Vehiculo)
    def __init__(self, x, y, rutas_enemigos, scale=1.2):
        # Llama al constructor de la clase base y pasar la imagen aleatoria
        if rutas_enemigos and len(rutas_enemigos) > 0:
            super().__init__(self.obtener_imagen_aleatoria(rutas_enemigos), x, y, scale)

    # Método para obtener una imagen aleatoria de la lista de rutas de enemigos
    def obtener_imagen_aleatoria(self, rutas_enemigos):
        # Selecciona aleatoriamente una ruta de la lista
        nombre_archivo = random.choice(rutas_enemigos)
        # Carga la imagen correspondiente a la ruta seleccionada
        return pygame.image.load(nombre_archivo)

    # Método para mover el vehículo hacia abajo en la pantalla
    def mover_vehiculo(self, speed):
        self.rect.y += speed

    # Método para actualizar la posición del vehículo y la puntuación del juego
    def actualizar(self, speed, score):
        # Mover el vehículo hacia abajo
        self.mover_vehiculo(speed)
        
        # Quita el vehículo de la pantalla una vez que sale de la pantalla
        if self.rect.top >= ALTO_VENTANA:
            self.kill()  # Elimina el objeto de la lista de sprites
            # Suma a la puntuación del jugador
            score += 10
        return score  # Devuelve la puntuación actualizada

