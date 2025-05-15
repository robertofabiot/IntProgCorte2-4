import os
import time 

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

print("Registro de asistencia UAM")
time.sleep(3)

asistencia_seccion = [0]*3

for seccion in range (3):
    print(f"Sección: {seccion+1}")
    for dia in dias:
        print(f"Día: {dia}")
        asistencias_registrada = 0
        for estudiante in range (1, 7):
            presente = int(input(f"""El estudiante {estudiante} está...
[1] Presente
[2] Ausente
"""))
            if presente == 1:
                asistencias_registrada += 1
        asistencia_seccion[seccion] += asistencias_registrada
        os.system('cls')
    os.system('cls')

total_general = sum(asistencia_seccion)

print("Generando asistencia...")
time.sleep(1.5)

for seccion in range (3):
    print(f"El total de la sección {seccion+1} fue: {asistencia_seccion[seccion]}")
print(f"El total general de la semana fue: {total_general}")