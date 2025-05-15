#Importar librerías necesarias
import os
import time 

#Crear lista de días de la semana, útil para imprimirlos en pantalla
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

print("Registro de asistencia UAM")
time.sleep(3)

#Crear una lista con tres ceros, representando la asistencia de cada sección
totales_por_seccion = [0]*3

for seccion in range (3): #Evalúa para cada sección
    for dia in dias: #Evalúa para cada día en la lista
        print(f"Sección: {seccion+1}")
        print(f"Día: {dia}")
        asistencias_del_dia = 0
        for estudiante in range (1, 7): #Recorre a los 6 estudiantes de la sección para registrar su asistencia del día
            while True: #Validación de datos
                try:
                    respuesta = int(input(f"""El estudiante {estudiante} está... 
[1] Presente
[2] Ausente
"""))
                    if respuesta not in range(1, 3): #Si el valor ingresado no está en el rango entre 1 y 2, genera un ValueError
                        raise ValueError()
                    break
                except ValueError: #Imprime un mensaje si se da un ValueError, generado por ingresar texto, decimales, o manualmente como en el caso anterior
                    print("Debe ingresar un 1 para Presente y un 2 para Ausente.")

#Suma 1 a la variable de la asistencia si está presente. Luego suma el total a la sección evaluándose
            if respuesta == 1: 
                asistencias_del_dia += 1
        totales_por_seccion[seccion] += asistencias_del_dia
        os.system('cls')
    os.system('cls')

#Obtiene el total general de la semana
total_general = sum(totales_por_seccion)

print("Generando asistencia...")
time.sleep(1.5)

#Mostrar resultados
for seccion in range (3):
    print(f"El total de la sección {seccion+1} fue: {totales_por_seccion[seccion]}")
print(f"El total general de la semana fue: {total_general}")