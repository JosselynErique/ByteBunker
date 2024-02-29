# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (3 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad QUITO 1
        [   # Semana 1
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 10},
            {"day": "Domingo", "temp": 11}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 25}
        ],

    ],
    [   # Ciudad JOYA DE LOS SACHAS 2
        [   # Semana 1
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 30}
        ],

    ],
    [   # Ciudad PUYO  3
        [   # Semana 1
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 16}
        ],

    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print(suma)