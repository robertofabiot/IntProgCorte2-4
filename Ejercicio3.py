# Definimos la cantidad de días, stands y productos
dias = 3
stands = 4
productos = 3

# Variable para acumular el total general de la feria
total_general = 0

# Bucle para cada día de la feria
for dia in range(1, dias + 1):
    print(f"\nDía {dia}")
    total_dia = 0  # Acumulador para el total del día
    # Bucle para cada stand en el día actual
    for stand in range(1, stands + 1):
        print(f"  Stand {stand}")
        total_stand = 0  # Acumulador para el total del stand
        # Bucle para cada producto en el stand actual
        for producto in range(1, productos + 1):
            # Pedimos al usuario el monto de venta para el producto
            monto = 3 
            total_stand += monto  # Sumamos el monto al total del stand
        print(f"    Total ventas Stand {stand}: {total_stand}")
        total_dia += total_stand  # Sumamos el total del stand al total del día
    print(f"  Total del día {dia}: {total_dia}")
    total_general += total_dia  # Sumamos el total del día al total general

# Mostramos el total general de la feria
print(f"\nTotal general de la feria: {total_general}")