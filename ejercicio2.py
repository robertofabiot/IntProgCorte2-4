# Programa para simular el uso de computadoras en dos laboratorios
# Permite ingresar 'o' para Ocupada y 'l' para Libre como abreviaciones

from date import datetime
# Definición de dimensiones de los laboratorios
filas = 5  # Número de filas en cada laboratorio
columnas = 4  # Número de computadoras por fila
num_laboratorios = 2  # Número de laboratorios
laboratorios = []  # Lista para guardar los estados de los laboratorios

# Ciclo para ingresar datos de cada laboratorio
for lab in range(1, num_laboratorios + 1):
    print(f"\nIngresando datos para el Laboratorio {lab}:")
    laboratorio = []  # Lista para almacenar el estado de las computadoras en este laboratorio
    contador_pc = 1  # Contador para número de computadora en el laboratorio
    for fila in range(filas):
        fila_estado = []  # Lista para almacenar el estado de las computadoras en esta fila
        for col in range(columnas):
            # Validar el estado de la computadora ingresado por el usuario
            while True:
                # Solicitar al usuario que ingrese el estado de la computadora con número secuencial
                estado = input(f"Ingrese el estado de la computadora #{contador_pc} en Laboratorio {lab}, fila {fila + 1}, columna {col + 1} (Ocupada[o]/Libre[l]): ").strip().lower()
                # Verificar si la entrada es válida (acepta 'o', 'ocupada', 'l', 'libre')
                if estado in ['o', 'ocupada']:
                    estado_pc = 'Ocupada'
                    break  # Entrada válida, salir del bucle
                elif estado in ['l', 'libre']:
                    estado_pc = 'Libre'
                    break  # Entrada válida, salir del bucle
                else:
                    # Mensaje de error si la entrada no es válida
                    print("Entrada inválida. Por favor ingrese 'o' para Ocupada o 'l' para Libre.")
            # Agregar el estado de la computadora a la fila
            fila_estado.append(estado_pc)
            contador_pc += 1  # Incrementar contador de computadoras
        # Agregar la fila completa al laboratorio
        laboratorio.append(fila_estado)
    # Agregar el laboratorio completo a la lista de laboratorios
    laboratorios.append(laboratorio)

# Mostrar resumen del uso de computadoras
print("\nResumen del uso de computadoras:")

# Ciclo para mostrar el resumen de cada laboratorio
for i, laboratorio in enumerate(laboratorios):
    ocupadas = 0  # Contador para computadoras ocupadas
    libres = 0  # Contador para computadoras libres
    # Contar computadoras ocupadas y libres en el laboratorio
    for fila in laboratorio:
        for estado in fila:
            if estado == 'Ocupada':
                ocupadas += 1  # Incrementar contador de ocupadas
            else:
                libres += 1  # Incrementar contador de libres
    # Mostrar el resumen para el laboratorio actual
    print(f"\nLaboratorio {i + 1}:")
    print(f"Computadoras Ocupadas: {ocupadas}")
    print(f"Computadoras Libres: {libres}")

# Mostrar el estado completo de cada laboratorio
for i, laboratorio in enumerate(laboratorios):
    print(f"\nEstado completo del Laboratorio {i + 1}:")
    for fila in laboratorio:
        # Mostrar el estado de cada fila, separando los estados con " | "
        print(" | ".join(fila)) 
    print()  # Línea en blanco para mejor legibilidad
# Fin del programa