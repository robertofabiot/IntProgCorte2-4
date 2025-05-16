def obtener_estado_pc(fila, columna, laboratorio_num):
    # Función para obtener el estado de una computadora en un laboratorio específico
    while True:
        # Solicita al usuario que ingrese el estado de la computadora
        estado = input(f"Ingrese el estado de la computadora en Laboratorio {laboratorio_num}, fila {fila + 1}, columna {columna + 1} (Ocupada/Libre): ").strip().lower()
        # Verifica si la entrada es válida
        if estado in ['ocupada', 'libre']:
            return 'Ocupada' if estado == 'ocupada' else 'Libre'
        else:
            print("Entrada inválida. Por favor ingrese 'Ocupada' o 'Libre'.")

def contar_computadoras(laboratorio):
    # Función para contar cuántas computadoras están ocupadas y cuántas están libres
    ocupadas = sum(estado == 'Ocupada' for fila in laboratorio for estado in fila)
    libres = sum(estado == 'Libre' for fila in laboratorio for estado in fila)
    return ocupadas, libres

def main():
    # Definimos las dimensiones de los laboratorios
    filas = 5
    columnas = 4
    num_laboratorios = 2
    laboratorios = []  # Lista para almacenar los laboratorios

    # Ciclo para ingresar datos de cada laboratorio
    for lab in range(1, num_laboratorios + 1):
        print(f"\nIngresando datos para el Laboratorio {lab}:")
        laboratorio = []  # Lista para almacenar el estado de las computadoras en el laboratorio
        for fila in range(filas):
            fila_estado = []  # Lista para almacenar el estado de las computadoras en la fila
            for col in range(columnas):
                # Llama a la función para obtener el estado de cada computadora
                estado_pc = obtener_estado_pc(fila, col, lab)
                fila_estado.append(estado_pc)  # Agrega el estado a la fila
            laboratorio.append(fila_estado)  # Agrega la fila al laboratorio
        laboratorios.append(laboratorio)  # Agrega el laboratorio a la lista de laboratorios

    print("\nResumen del uso de computadoras:")

    # Ciclo para mostrar el resumen de cada laboratorio
    for i, laboratorio in enumerate(laboratorios):
        ocupadas, libres = contar_computadoras(laboratorio)  # Cuenta las computadoras ocupadas y libres
        print(f"\nLaboratorio {i + 1}:")
        print(f"Computadoras Ocupadas: {ocupadas}")
        print(f"Computadoras Libres: {libres}")

    # Mostrar estado detallado opcional
    for i, laboratorio in enumerate(laboratorios):
        print(f"\nEstado completo del Laboratorio {i + 1}:")
        for fila in laboratorio:
            print(" | ".join(fila))  # Muestra el estado de cada fila
        print()

# Punto de entrada del programa
if __name__ == "__main__":
    main()
