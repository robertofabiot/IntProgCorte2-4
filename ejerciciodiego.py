# Crear lista de días de la semana, útil para imprimirlos en pantalla
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Crear lista con cuatro ceros, representando el consumo de kilovatios total de cada edificio
consumos_totales_por_edificio = [0] * 4

print("Monitoreo de Consumo Energético de Edificios")

# Recorrer cada edificio
for edificio in range(4):
    print(f"\nEdificio {edificio + 1}:")
    # Recorrer cada día de la semana
    for dia in dias:
        print(f"\nDía: {dia}")
        consumo_del_dia = 0
        # Recorrer los tres turnos (mañana, tarde, noche)
        for turno in ["mañana", "tarde", "noche"]:
            while True:  # Validación de datos
                try:
                    # Solicitar el consumo por turno
                    consumo = float(input(f"Ingrese el consumo de kilovatios en la {turno} del edificio {edificio + 1}: "))
                    if consumo < 0:  # Validación para asegurarse de que el consumo no sea negativo
                        raise ValueError("El consumo no puede ser negativo.")
                    break
                except ValueError:
                    print(f"Error. Por favor, ingrese un valor válido para el consumo.")
            
            # Sumar el consumo del turno al consumo total del día
            consumo_del_dia += consumo
        
        # Sumar el consumo del día al consumo total del edificio
        consumos_totales_por_edificio[edificio] += consumo_del_dia

# Calcular el promedio semanal para cada edificio
for edificio in range(4):
    promedio_semanal = consumos_totales_por_edificio[edificio] / 7
    # Mostrar resultados
    print(f"\nResultados del consumo energético del edificio {edificio + 1}:")
    print(f"Consumo total del edificio {edificio + 1}: {consumos_totales_por_edificio[edificio]} kW")
    print(f"Promedio semanal del edificio {edificio + 1}: {promedio_semanal:.2f} kW")

#Calcula y muestra el promedio general
print(f"El promedio general fue {sum(consumos_totales_por_edificio)/4}")