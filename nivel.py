import pygame
from pygame.locals import *
from constantesCar import *
from logica_inicial import Juego


class Nivel:
    # Constructor de la clase Nivel
    def __init__(self, numero, rutas_enemigos, color_fondo, tiempo_nivel, player_x=250, player_y=400):
        # Inicializa atributos del nivel
        self.numero = numero
        self.rutas_enemigos = rutas_enemigos
        self.color_fondo = color_fondo
        self.tiempo_nivel = tiempo_nivel
        self.player_x = player_x
        self.player_y = player_y
        self.juego = None  # Este atributo se inicializa en None y podría ser utilizado para almacenar una instancia de Juego

  
    def cargar_niveles(nivel: int, tiempo_nivel: int):
        rutas_enemigos = []
        color_fondo = None

        # Configura los niveles
        if nivel == 1:
            rutas_enemigos = ['programacion\ejercicios\juego_2\imagenes\carVerde.png', 'programacion\ejercicios\juego_2\imagenes\carPremio.png']
            color_fondo = COLOR_VERDE
        elif nivel == 2:
            rutas_enemigos = ['programacion\ejercicios\juego_2\imagenes\carVerde.png', 'programacion\ejercicios\juego_2\imagenes\camioneta.png', 'programacion/ejercicios/pygame/carAmarillo.png', 'programacion\ejercicios\juego_2\imagenes\camion.png']
            color_fondo = COLOR_CYAN
        elif nivel == 3:
            rutas_enemigos = ['programacion\ejercicios\juego_2\imagenes\car_fire.png', 'programacion\ejercicios\juego_2\imagenes\carPremio.png', 'programacion\ejercicios\juego_2\imagenes\sanidad.png', 'programacion\ejercicios\juego_2\imagenes\camion.png']
            color_fondo = COLOR_PURPURA

        # Ejecuta el nivel y pasa el puntaje acumulado
        nivel = Juego.ejecutar_nivel(rutas_enemigos, color_fondo, tiempo_nivel)
        return nivel
    
    
    def obtener_tiempo_nivel(nivel: int):
        if nivel == 1:
            return 20
        elif nivel == 2:
            return 30
        elif nivel == 3:
            return 40
        return 0


