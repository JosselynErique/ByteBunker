# Crear el diccionario con información personal ficticia
informacion_personal = {
    "nombre": "JOSSELYN",
    "edad": 29,
    "ciudad": "JOYA DE LOS SACHAS",
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "JOYA DE LOS SACHAS"

# Agregar una nueva clave-valor representando la profesión
informacion_personal["profesion"] = "Doctora"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0989485106"

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad")

# Imprimir el diccionario final
print("Diccionario Final:")
print(informacion_personal)
