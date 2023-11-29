import json

#función para leer datos desde un archivo JSON
def leer_data(archivo: str) -> list:
    #utiliza un bloque 'with' para garantizar que el archivo se cierre correctamente después de su uso
    with open(archivo, "r", encoding='utf-8') as file:
        data = json.load(file)  # Convierte el JSON en un diccionario de Python

    # Obtiene la lista de puntuaciones del diccionario o una lista vacía si no hay datos
    list_score = data.get("ranking", [])

    return list_score

# Define una función para guardar datos en un archivo JSON
def guardar_data(ranking: list, name: str, score: int):
    # Agrega una nueva entrada al ranking
    ranking.append({"name": name, "score": score})

    # Abre el archivo en modo de escritura y escribir el nuevo ranking en formato JSON
    with open("programacion\ejercicios\pygame\data.json", 'w', encoding='utf-8') as file:
        json.dump({"ranking": ranking}, file, indent=4)
