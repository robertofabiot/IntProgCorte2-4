#Ejercicio 4: Monitoreo del consumo energético 
# Desarrolle un programa que registre el consumo energético de cuatro edificios del campus 
# universitario a lo largo de una semana. Por cada día se ingresarán los kilovatios consumidos en 
# tres turnos: mañana, tarde y noche. El programa debe calcular el consumo total por edificio y 
# generar el promedio semanal correspondiente. 

kilovatios_mañana = (int(input("Ingrese el consumo de kilovatios en la mañana en del edificio 1: ")),
               int(input("Ingrese el consumo de kilovatios en la mañana del edificio 2: ")),
               int(input("Ingrese el consumo de kilovatios en la mañana del edificio 3: ")),
               int(input("Ingrese el consumo de kilovatios en la mañana del edificio 4: ")))

kilovatios_tarde = (int(input("Ingrese el consumo de kilovatios en la tarde del edificio 1: ")),
                int(input("Ingrese el consumo de kilovatios en la tarde del edificio 2: ")),
                int(input("Ingrese el consumo de kilovatios en la tarde del edificio 3: ")),
                int(input("Ingrese el consumo de kilovatios en la tarde del edificio 4: ")))

kilovatios_noche = (int(input("Ingrese el consumo de kilovatios en la noche del edificio 1: ")),
                int(input("Ingrese el consumo de kilovatios en la noche del edificio 2: ")),
                int(input("Ingrese el consumo de kilovatios en la noche del edificio 3: ")),
                int(input("Ingrese el consumo de kilovatios en la noche del edificio 4: ")))

# Calcular el consumo total por edificio
consumo_total_edificio1 = kilovatios_mañana[0] + kilovatios_tarde[0] + kilovatios_noche[0]
consumo_total_edificio2 = kilovatios_mañana[1] + kilovatios_tarde[1] + kilovatios_noche[1]
consumo_total_edificio3 = kilovatios_mañana[2] + kilovatios_tarde[2] + kilovatios_noche[2]
consumo_total_edificio4 = kilovatios_mañana[3] + kilovatios_tarde[3] + kilovatios_noche[3]

# Calcular el promedio semanal
promedio_semanal_edificio1 = consumo_total_edificio1 / 7
promedio_semanal_edificio2 = consumo_total_edificio2 / 7
promedio_semanal_edificio3 = consumo_total_edificio3 / 7
promedio_semanal_edificio4 = consumo_total_edificio4 / 7

# Mostrar resultados
print("\nResultados del consumo energetico: \n")
print("Consumo total del edificio 1:", consumo_total_edificio1, "kW")
print("Promedio semanal del edificio 1:", promedio_semanal_edificio1, "kW")
print("\nConsumo total del edificio 2:", consumo_total_edificio2, "kW")
print("Promedio semanal del edificio 2:", promedio_semanal_edificio2, "kW")
print("\nConsumo total del edificio 3:", consumo_total_edificio3, "kW")
print("Promedio semanal del edificio 3:", promedio_semanal_edificio3, "kW")
print("\nConsumo total del edificio 4:", consumo_total_edificio4, "kW")
print("Promedio semanal del edificio 4:", promedio_semanal_edificio4, "kW")
