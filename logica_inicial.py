import pygame
from pygame.locals import *
import random
from constantesCar import *
from vehiculo import PlayerCar
from vehiculo_enemigo import VehiculoEnemigo
from carretera import Carretera
from menu import *
from funcion import *
from control_juego import *


# barra de score
barra_score = pygame.image.load("programacion\ejercicios\juego_2\imagenes\linea_score.png")
barra_score = pygame.transform.scale(barra_score, (ANCHO_VENTANA, 50))

# Coordenadas de los carriles
carril_izquierdo = 150
carril_central = 250
carril_derecho = 350
carriles = [carril_izquierdo, carril_central, carril_derecho]

class Juego:
    def __init__(self):
        pygame.init()

        # Ventana principal
        self.screen = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])
        pygame.display.set_caption("Cars on Road - Verónica Castillo")

        # Coordenadas iniciales del jugador
        self.player_x = 250
        self.player_y = 400

        # Configuración de la pantalla
        self.clock = pygame.time.Clock()
        self.fps = 60

        # Color de fondo predeterminado
        self.color_fondo = COLOR_VERDE

        # Llamada a la función de inicialización
        self.inicializar_juego()

        self.rutas_enemigos = None  # Inicializar como None
        
        self.nivel_completado = False
        self.score = 0
        self.iniciales = "" 


    def inicializar_juego(self):
        # Configuración del juego
        self.gameover = False
        
        #self.speed = 2 

        # Atributo para el puntaje acumulado
        self.puntaje_acumulado = 0

        # Tiempo total niveles (en segundos)
        self.tiempo_nivel = 60 
        self.tiempo_transcurrido = 0

        # Número de niveles completados
        self.niveles_completados = 0

        # Grupos de sprites
        self.player_group = pygame.sprite.Group()
        self.vehicle_group = pygame.sprite.Group()

        # Crear el auto del jugador
        self.player = PlayerCar(self.player_x, self.player_y, scale=0.4)
        self.player_group.add(self.player)

        # Cargar la imagen de colisión
        self.explosion = pygame.image.load("programacion\ejercicios\juego_2\imagenes\explosion.png")
        self.explosion = pygame.transform.scale(self.explosion, (ANCHO_EXPLOSION, ALTO_EXPLOSION))
        self.rectangulo_choque = self.explosion.get_rect()

        # Crear la carretera
        self.carretera = Carretera()
    
    def aumentar_velocidad(self, score, speed):
    # Aumentar la velocidad después de pasar cierta cantidad de vehículos
        if score > 0 and score % 30 == 0:
            speed += 0.003
        return speed
    
    def manejar_eventos(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if not self.gameover:
                    if event.key == K_LEFT and self.player.rect.center[0] > carril_izquierdo:
                        self.player.rect.x -= 100
                    elif event.key == K_RIGHT and self.player.rect.center[0] < carril_derecho:
                        self.player.rect.x += 100
                   

    def actualizar_juego(self):
        self.carretera.actualizar(self.speed)
        # Comprobar si hay una colisión al cambiar de carril
        for enemy_car in self.vehicle_group:
            if pygame.sprite.collide_rect(self.player, enemy_car):
                self.gameover = True
                # Colocar el auto del jugador al lado del otro vehículo
                # y determinar dónde colocar la imagen de colisión
                if pygame.key.get_pressed()[K_LEFT]:
                    self.player.rect.left = enemy_car.rect.right
                    self.rectangulo_choque.center = [self.player.rect.left, (self.player.rect.center[1] + enemy_car.rect.center[1]) / 2]
                    self.screen.blit(self.explosion, self.rectangulo_choque)
                elif pygame.key.get_pressed()[K_RIGHT]:
                    self.player.rect.right = enemy_car.rect.left
                    self.rectangulo_choque.center = [self.player.rect.right, (self.player.rect.center[1] + enemy_car.rect.center[1]) / 2]
                    self.screen.blit(self.explosion, self.rectangulo_choque)

        # Sumar el puntaje al acumulado
        self.puntaje_acumulado += self.score
        
        # Aumentar la velocidad
        self.speed = self.aumentar_velocidad(self.score, self.speed)


    def ejecutar_nivel(rutas_enemigos, color_fondo, tiempo_nivel):
        # Crea una instancia del juego
        juego = Juego()

        # Cambia el color de fondo
        juego.cambiar_color_fondo(color_fondo)

        # Establece rutas_enemigos antes de ejecutar el juego
        juego.rutas_enemigos = rutas_enemigos

        # Ejecuta el juego y ajustar el tiempo del nivel
        nivel_completado = ControladorJuego.ejecutar_juego(tiempo_nivel)
        return nivel_completado
    
    def cambiar_color_fondo(self, nuevo_color):
        # Dibujar el césped
        self.screen.fill(nuevo_color)
    
    def dibujar_pantalla(self):
        # Dibujar la carretera
        self.carretera.dibujar(self.screen, [150, 250, 350])

        # Dibujar el auto del jugador
        self.player_group.draw(self.screen)

        # Agregar un vehículo enemigo
        if len(self.vehicle_group) < 2 and all(enemy_car.rect.top >= enemy_car.rect.height * 1.5 for enemy_car in self.vehicle_group):
            lane = random.choice([150, 250, 350])
            enemy_car = VehiculoEnemigo(lane, ALTO_VENTANA / -2, self.rutas_enemigos, scale=0.5)
            self.vehicle_group.add(enemy_car)

        # Actualizar los vehículos
        for enemy_car in self.vehicle_group:
            self.score = enemy_car.actualizar(self.speed, self.score)

        # Dibuja los vehículos
        self.vehicle_group.draw(self.screen)

        # Dibuja la barra de score
        self.screen.blit(barra_score, (0, 0))

        # Muestra el puntaje en la pantalla
        font = pygame.font.SysFont("Arial Narrow", 35)
        text = font.render('Score: ' + str(self.score), True, COLOR_NEGRO)
        text_rect = text.get_rect()
        text_rect.center = (400, 25)
        self.screen.blit(text, text_rect)

        # Comprueba si hay una colisión de frente
        if pygame.sprite.spritecollide(self.player, self.vehicle_group, True):
            self.gameover = True
            self.rectangulo_choque.center = [self.player.rect.center[0], self.player.rect.top]
            self.screen.blit(self.explosion, self.rectangulo_choque) 
        
        # muestra el fin del juego
        if self.gameover:
            self.screen.blit(self.explosion, self.rectangulo_choque)
            pygame.draw.rect(self.screen, COLOR_ROSA, (100, 250, 300, 100))
            font = pygame.font.Font(pygame.font.get_default_font(), 14)
            text_rect = text.get_rect()
            text = font.render('GAME OVER - Play again? (Enter Y or N)', True, COLOR_NEGRO)
            text_rect.center = (ANCHO_VENTANA / 3.1, 290)
            self.screen.blit(text, text_rect)

        pygame.display.update()


        
        pygame.quit()  

"""   
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






def ejecutar_juego(self, tiempo_nivel):
        running = True
        tiempo_inicio = pygame.time.get_ticks()  # Obtener el tiempo de inicio en milisegundos
        #read ranking
        ranking = leer_data("programacion\ejercicios\juego_2\data.json")

        # Verifica si se ha producido una colisión
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            if not self.gameover:
                self.clock.tick(self.fps)
                self.manejar_eventos()
                self.actualizar_juego()
                self.dibujar_pantalla()

            # Esperar la entrada del usuario para jugar de nuevo o salir
            while self.gameover:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.gameover = False
                        running = False
                    elif event.type == KEYDOWN:
                        if event.key == K_y:
                            # Reiniciar el juego
                            self.gameover = False
                            self.speed = 2
                            self.score = 0
                            self.vehicle_group.empty()
                            self.player.rect.center = [self.player_x, self.player_y]
                        elif event.key == K_n:
                            # Salir de los bucles
                            guardar_data(ranking)
                            self.gameover = False
                            running = False

                # Verifica el tiempo transcurrido
                tiempo_actual = pygame.time.get_ticks()
                tiempo_transcurrido_segundos = (tiempo_actual - tiempo_inicio) // 1000

                # Si el tiempo del nivel ha transcurrido, establecer nivel_completado en True
                if tiempo_transcurrido_segundos >= tiempo_nivel:
                    self.nivel_completado = True
                    
                # Verifica si el jugador ha completado el nivel
                tiempo_transcurrido_segundos = (pygame.time.get_ticks() - tiempo_inicio) // 1000
                if self.niveles_completados < 3 and tiempo_transcurrido_segundos >= tiempo_nivel:
                    self.niveles_completados += 1
                    puntaje_acumulado += self.score  # Sumar el puntaje al acumulado
                    print(self.score)"""