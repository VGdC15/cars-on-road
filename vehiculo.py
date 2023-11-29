import pygame

# clase Vehiculo que hereda de pygame.sprite.Sprite
class Vehiculo(pygame.sprite.Sprite):

    # Constructor de la clase, recibe una imagen, coordenadas (x, y) y una escala opcional
    def __init__(self, image, x, y, scale=1.0):
        # Llama al constructor de la clase base (pygame.sprite.Sprite)
        pygame.sprite.Sprite.__init__(self)

        # Calcula las nuevas dimensiones de la imagen según la escala
        nuevo_ancho = int(image.get_rect().width * scale)
        nuevo_alto = int(image.get_rect().height * scale)
        
        # Escala la imagen
        self.image = pygame.transform.scale(image, (nuevo_ancho, nuevo_alto))

        # Obtiene el rectángulo que rodea la imagen y centrarlo en las coordenadas (x, y)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

# Define una subclase llamada PlayerCar que hereda de la clase Vehiculo
class PlayerCar(Vehiculo):

    # Constructor de la subclase, recibe las coordenadas (x, y) y una escala opcional
    def __init__(self, x, y, scale=1.0):
        # Carga la imagen del jugador desde un archivo
        image = pygame.image.load('programacion\ejercicios\pygame\PlayerCar.png')
        # Llama al constructor de la clase base (Vehiculo) y pasar la imagen, coordenadas y escala
        super().__init__(image, x, y, scale)
