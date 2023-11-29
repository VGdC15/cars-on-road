from logica_inicial import Juego
import pygame
from nivel import Nivel
from pygame.locals import *

class ControladorJuego(Juego):
    def __init__(self,ranking):
        super().__init__()  # Llama al constructor de la clase base (Juego)
        self.ranking = ranking  # Almacena el ranking como un atributo
        self.nivel_actual = 1

    def iniciar_juego(self):
        while self.nivel_actual <= 3:
            tiempo_nivel = Nivel.obtener_tiempo_nivel(self.nivel_actual)
            print(f"Iniciando nivel {self.nivel_actual}, tiempo: {tiempo_nivel} segundos")

            # Pasa el puntaje acumulado al cargar_niveles
            nivel_completado = Nivel.cargar_niveles(self.nivel_actual, tiempo_nivel)

            if nivel_completado:
                print(f"Nivel {self.nivel_actual} completado")
                self.nivel_actual += 1
            else:
                print(f"Nivel {self.nivel_actual} no completado, saliendo del bucle")
                break
    
    def ejecutar_juego(self):
        nivel_actual = 1
        puntaje_acumulado = 0

        while nivel_actual <= 3:
            tiempo_nivel = Nivel.obtener_tiempo_nivel(nivel_actual)
            print(f"Iniciando nivel {nivel_actual}, tiempo: {tiempo_nivel} segundos")

            # Restablecer variables para el nuevo nivel
            self.gameover = False
            tiempo_inicio_nivel = pygame.time.get_ticks()  # Obtener el tiempo de inicio en milisegundos
            self.speed = 2
            self.score = 0
            self.vehicle_group.empty()
            self.player.rect.center = [self.player_x, self.player_y]

            while not self.gameover:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.gameover = True

                self.clock.tick(self.fps)
                self.manejar_eventos()
                self.actualizar_juego()
                self.dibujar_pantalla()

                # Verifica el tiempo transcurrido
                tiempo_actual = pygame.time.get_ticks()
                tiempo_transcurrido_segundos = (tiempo_actual - tiempo_inicio_nivel) // 1000

                # Si el tiempo del nivel ha transcurrido, establecer gameover en True
                if tiempo_transcurrido_segundos >= tiempo_nivel:
                    self.gameover = True

            # Verifica si el jugador ha completado el nivel
            if not self.gameover:
                puntaje_acumulado += self.score  # Sumar el puntaje al acumulado
                print(f"Nivel {nivel_actual} completado. Puntaje acumulado: {puntaje_acumulado}")

            nivel_actual += 1

