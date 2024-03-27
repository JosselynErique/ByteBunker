# Creación del archivo de notas
with open("my_notes.txt", "w") as file:
    # Escribiendo notas en el archivo
    file.write("1. Realizar las tareas de la semana.\n")
    file.write("2. Ir a reunion de la escuela de David.\n")
    file.write("3. Ir a coger cita para el control de Matias.\n")

# Lectura del archivo de notas
with open("my_notes.txt", "r") as file:
    # Leer contenido línea por línea
    for line in file:
        # Mostrar cada línea en la consola
        print(line.strip())

# Cierre del archivo
file.close()
