import os, time, funx
while True:
    os.system("cls")
    print("Bienvenido.")
    print("1. Mostrar asientos disponibles")
    print("2. Comprar asiento")
    print("3. Mostrar compras realizadas")
    print("4. Exportar como CSV")
    print("5. Salir")
    try:
        opc = int(input("Ingrese opción: "))
    except:
        print("ERROR! Debe ingresar un número!")
    if opc in range(1,6):
        if opc == 1:
            pass
        elif opc == 2:
            pass
        elif opc == 3:
            pass
        elif opc == 4:
            pass
        elif opc == 5:
            break
    else:
        print("Opción inválida.")
        time.sleep(1)