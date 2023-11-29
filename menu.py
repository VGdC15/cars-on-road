import pygame
from constantesCar import *
from funcion import *
from control_juego import *



FPS = 60 

def ejecutar_menu(ranking):
    iniciales = ""  # almacena las iniciales del jugador

    pygame.init()  

    # Crea la ventana de juego
    screen = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])
    pygame.display.set_caption("Cars on Road - Verónica Castillo")

    # Carga y ajusta la imagen de fondo del menú principal
    imagen_fondo = pygame.image.load("programacion\ejercicios\juego_2\imagenes\menu.png")
    imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

    # Carga y ajusta la imagen del botón start
    boton_start = pygame.image.load("programacion\ejercicios\juego_2\imagenes\start.png")
    boton_start = pygame.transform.scale(boton_start, (ANCHO_BOTON, ALTO_BOTON))
    rect_boton_start = boton_start.get_rect()
    rect_boton_start.x = -45
    rect_boton_start.y = 385

    # Carga y ajusta la imagen del botón ranking
    boton_ranking = pygame.image.load("programacion\ejercicios\juego_2\imagenes\score.png")
    boton_ranking = pygame.transform.scale(boton_ranking, (ANCHO_BOTON, ALTO_BOTON))
    rect_boton_ranking = boton_ranking.get_rect()
    rect_boton_ranking.x = 160
    rect_boton_ranking.y = 385

    # Dibuja un rectángulo blanco como fondo para el campo de texto de iniciales
    pygame.draw.rect(imagen_fondo, COLOR_BLANCO, (POSICION_X_RECTANGULO, POSICION_Y_RECTANGULO, ANCHO_RECTANGULO, ALTO_RECTANGULO))
    
    # Muestra un mensaje en la pantalla para indicar al jugador que ingrese sus iniciales
    font = pygame.font.Font(pygame.font.get_default_font(), 17)
    text = font.render('Ingrese sus iniciales:', True, COLOR_NEGRO)
    imagen_fondo.blit(text, (72, 350))

    clock = pygame.time.Clock()

    # Inicializa variables de control
    start_boton = False  # Variable que indica si se ha iniciado el juego
    ranking_boton = False  # Variable que indica si se ha seleccionado la opción de ranking
    
    run = True  #controla el bucle principal del menú
    while run:
        # Mostrar la imagen de fondo y los botones en la pantalla
        screen.blit(imagen_fondo, (0, 0))
        screen.blit(boton_start, rect_boton_start)
        screen.blit(boton_ranking, rect_boton_ranking)

        # Crear un objeto de fuente para mostrar el texto de ingreso de iniciales
        font = pygame.font.Font(pygame.font.get_default_font(), 24)
        text_ingreso = font.render(iniciales, True, COLOR_NEGRO)
        imagen_fondo.blit(text_ingreso, (POSICION_X_RECTANGULO + 10, POSICION_Y_RECTANGULO + 10))

        # Manejo de eventos de Pygame
        for evento in pygame.event.get():
            # Comprobar si se cerró la ventana
            if evento.type == pygame.QUIT:
                run = False
            # Comprobar si se hizo clic con el mouse
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Obtener la posición del clic
                posicion_click = list(evento.pos)
                # Comprobar si se hizo clic en el botón de inicio
                if rect_boton_start.collidepoint(posicion_click):
                    start_boton = True
                    run = False
                # Comprobar si se hizo clic en el botón de ranking
                elif rect_boton_ranking.collidepoint(posicion_click):
                    ranking_boton = True
                    run = False
            # Comprobar si se presionó una tecla
            if evento.type == pygame.KEYDOWN:
                iniciales = manejar_ingreso_iniciales(evento, iniciales)

        if start_boton:
            # Crea una instancia de ControladorJuego
            controlador = ControladorJuego(ranking)
            # Llama al método ejecutar_juego en la instancia
            controlador.ejecutar_juego()
            break
      
        elif ranking_boton:
            ejecutar_pantalla_ranking(ranking)
              
        pygame.display.flip()
        # Esperar un tiempo para alcanzar el FPS deseado
        clock.tick(FPS)

    pygame.quit()


# maneja el ingreso de iniciales
def manejar_ingreso_iniciales(evento, iniciales):
    if evento.key == pygame.KEYDOWN:
        if evento.key == pygame.K_BACKSPACE:
            iniciales = iniciales[:-1]

    elif evento.key == pygame.K_RETURN:
        # Guarda la cadena de iniciales en la variable 'name'
        name = iniciales
    elif len(iniciales) < 3 and evento.unicode:  # Limita a 3 caracteres
        # Agrega el carácter Unicode de la tecla presionada a la cadena de iniciales
        if len(iniciales) < 3:
            iniciales += evento.unicode

    return iniciales


def ejecutar_pantalla_ranking(ranking: list):
    pygame.init()  # Inicializa Pygame

    # Crea la ventana de juego
    screen = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])
    pygame.display.set_caption("Cars on Road - Verónica Castillo")

    # Carga y ajusta la imagen de fondo
    imagen_fondo = pygame.image.load("programacion\ejercicios\juego_2\imagenes\pantalla_ranking.png")
    imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

    # Carga y ajusta la imagen del botón del menú principal
    boton_menu_principal = pygame.image.load("programacion\ejercicios\juego_2\imagenes\menu_principal.png")
    boton_menu_principal = pygame.transform.scale(boton_menu_principal, (ANCHO_BOTON, ALTO_BOTON))
    rect_boton_menu_principal = boton_menu_principal.get_rect()
    rect_boton_menu_principal.x = 60
    rect_boton_menu_principal.y = 440

    menu_principal = False  # variable que indica si se debe ir al menú principal
    
    run = True
    while run:
        # Dibuja la imagen de fondo y el botón del menú principal en la pantalla
        screen.blit(imagen_fondo, (0, 0))
        screen.blit(boton_menu_principal, rect_boton_menu_principal)

        # Manejo de eventos
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Verifica si se hizo clic en el botón del menú principal
                posicion_click = list(evento.pos)
                if rect_boton_menu_principal.collidepoint(posicion_click):
                    menu_principal = True
                    run = False

        # Crea una fuente para mostrar el nombre y la puntuación en el ranking
        font_data = pygame.font.SysFont('Bauhaus 93', 30)
        for i in range(len(ranking)):
            # Renderiza el nombre del jugador en el ranking
            texto_name = font_data.render(ranking[i]["name"], True, COLOR_NEGRO)
            imagen_fondo.blit(texto_name, (160, 170 + i * 60))

            # Renderiza la puntuación del jugador en el ranking
            texto_score = font_data.render(str(ranking[i]["score"]), True, COLOR_NEGRO)
            imagen_fondo.blit(texto_score, (310, 170 + i * 60))

        # Actualiza la pantalla
        pygame.display.flip()

    # Si se debe ir al menú principal, llama a la función ejecutar_menu
    if menu_principal:
        ejecutar_menu(ranking)




