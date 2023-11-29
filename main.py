from menu import *
from funcion import *
from logica_inicial import *




"""def main():
    controlador = ControladorJuego()
    controlador.iniciar_juego()

if __name__ == "__main__":
    main()"""

if __name__ == "__main__":
    #read ranking
    ranking = leer_data("programacion\ejercicios\pygame\data.json")
    print(ranking)
    ejecutar_menu(ranking)
