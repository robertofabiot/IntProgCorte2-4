def obtener_estado_pc(fila, columna, laboratorio_num):
    while True:
        estado = input(f"Ingrese el estado de la computadora en Laboratorio {laboratorio_num}, fila {fila + 1}, columna {columna + 1} (Ocupada/Libre): ").strip().lower()
        if estado in ['ocupada', 'libre']:
            return 'Ocupada' if estado == 'ocupada' else 'Libre'
        else:
            print("Entrada inválida. Por favor ingrese 'Ocupada' o 'Libre'.")

def contar_computadoras(laboratorio):
    ocupadas = sum(estado == 'Ocupada' for fila in laboratorio for estado in fila)
    libres = sum(estado == 'Libre' for fila in laboratorio for estado in fila)
    return ocupadas, libres

def main():
    filas = 5
    columnas = 4
    num_laboratorios = 2
    laboratorios = []

    for lab in range(1, num_laboratorios + 1):
        print(f"\nIngresando datos para el Laboratorio {lab}:")
        laboratorio = []
        for fila in range(filas):
            fila_estado = []
            for col in range(columnas):
                estado_pc = obtener_estado_pc(fila, col, lab)
                fila_estado.append(estado_pc)
            laboratorio.append(fila_estado)
        laboratorios.append(laboratorio)

    print("\nResumen del uso de computadoras:")

    for i, laboratorio in enumerate(laboratorios):
        ocupadas, libres = contar_computadoras(laboratorio)
        print(f"\nLaboratorio {i + 1}:")
        print(f"Computadoras Ocupadas: {ocupadas}")
        print(f"Computadoras Libres: {libres}")

    # Mostrar estado detallado opcional
    for i, laboratorio in enumerate(laboratorios):
        print(f"\nEstado completo del Laboratorio {i + 1}:")
        for fila in laboratorio:
            print(" | ".join(fila))
        print()

if __name__ == "__main__":
    main()
