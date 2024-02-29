# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (3 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 40},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 36},
            {"day": "Jueves", "temp": 34},
            {"day": "Viernes", "temp": 36},
            {"day": "Sábado", "temp": 42},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 24}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 36},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 29}
        ],

    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 45},
            {"day": "Viernes", "temp": 48},
            {"day": "Sábado", "temp": 54},
            {"day": "Domingo", "temp": 52}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 55},
            {"day": "Jueves", "temp": 54},
            {"day": "Viernes", "temp": 48},
            {"day": "Sábado", "temp": 47},
            {"day": "Domingo", "temp": 56}
        ],

    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 49},
            {"day": "Martes", "temp": 54},
            {"day": "Miércoles", "temp": 45},
            {"day": "Jueves", "temp": 48},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 64},
            {"day": "Domingo", "temp": 48}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 48},
            {"day": "Martes", "temp": 91},
            {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 78},
            {"day": "Viernes", "temp": 77},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 91},
            {"day": "Martes", "temp": 93},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 82},
            {"day": "Sábado", "temp": 879},
            {"day": "Domingo", "temp": 41}
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