# Definir usuarios y contraseñas en un diccionario
usuarios = {
    "usuario1": "usuario 1",  
    "usuario2": "usuario 2",
    "usuario3": "usuario 3"   
}

# Mensaje de bienvenida para los clientes
print("Bienvenido a la tienda de electrónicos")

# Función para validar el login del usuario
def login():
    intentos = 3  # Número máximo de intentos permitidos
    while intentos > 0:  # Mientras haya intentos disponibles
        usuario = input("Ingrese su nombre de usuario: ")  # Solicitar nombre de usuario
        contraseña = input("Ingrese su contraseña: ")  # Solicitar contraseña
        if usuario in usuarios and usuarios[usuario] == contraseña:  # Verificar si el usuario y contraseña son correctos
            print("Ingreso satisfactorio.")  # Mensaje de éxito
            return True  # Retornar True si el login es correcto
        else:
            intentos -= 1  # Contador para reducir el número de intentos restantes
            print(f"Usuario o contraseña incorrectos. Le quedan {intentos} intentos.")  # Mensaje de error
    print("Ha excedido el número de intentos. Saliendo de la plataforma.")  # Mensaje si se agotan los intentos
    return False  # Retornar False si el login falla

# Función para registrar información del cliente
def registrar_informacion(): # Solicitar información del cliente, cada input es una solicitud de información diferente
    nombre = input("Ingrese su nombre completo: ")  
    cedula = input("Ingrese su cédula: ")  
    celular = input("Ingrese su número de celular: ")  
    correo = input("Ingrese su correo electrónico: ")  
    direccion = input("Ingrese su dirección: ")  
    return {  # Retornar un diccionario con la información del cliente
        "Nombre": nombre,
        "Cédula": cedula,
        "Celular": celular,
        "Correo": correo,
        "Dirección": direccion
    }

# Función para mostrar el menú de opciones
def menu():
    print("\nMenú de opciones:")  # Mostrar título del menú, la \n es un salto de línea
    print("1. Ventas de paquetes")  
    print("2. Horarios disponibles de atención")  
    print("3. Productos disponibles")  
    print("4. Historial de compras")  
    print("5. Facturación de compras")  
    opcion = input("Seleccione una opción: ")  # Solicitar al usuario que seleccione una opción
    return opcion  # Retornar la opción seleccionada

# Función para la venta de paquetes
def venta_paquetes(cliente):
    # Definir los paquetes disponibles con sus precios
    paquetes = {
        "1": {"nombre": "Set de componentes electrónicos", "precio": 15.000},
        "2": {"nombre": "Kit de soldadura con multímetro", "precio": 21.500},
        "3": {"nombre": "Set de bloques Robot Transformer", "precio": 31.500}
    }

    print("\nPaquetes disponibles:")  # Mostrar título de los paquetes
    for clave, valor in paquetes.items():  # Recorrer el diccionario de paquetes
        print(f"{clave}. {valor['nombre']} - ₡{valor['precio']:.3f}")  # Mostrar opciones

    try:
        opcion = input("Seleccione un paquete (1-3): ")  # Solicitar al usuario que elija un paquete
        if opcion in paquetes:  # Verificar si la opción es válida
            paquete_seleccionado = paquetes[opcion]  # Obtener el paquete seleccionado
            cantidad = int(input(f"Ingrese la cantidad de '{paquete_seleccionado['nombre']}' que desea comprar: "))  # Solicitar cantidad
            if cantidad > 0:  # Validar que la cantidad sea positiva
                subtotal = paquete_seleccionado["precio"] * cantidad  # Calcular subtotal
                iva = subtotal * 0.13  # Calcular IVA (13%)
                total = subtotal + iva  # Calcular total

                # Mostrar resumen de la compra
                print("\nResumen de la compra:")  
                print(f"Paquete seleccionado: {paquete_seleccionado['nombre']}")
                print(f"Cantidad: {cantidad}")
                print(f"Precio unitario: ₡{paquete_seleccionado['precio']:.3f}") #₡ es para indicar que es un valor monetario, .3f es para indicar que se muestren 3 decimales
                print(f"Subtotal: ₡{subtotal:.3f}") 
                print(f"IVA (13%): ₡{iva:.3f}")
                print(f"Total a pagar: ₡{total:.3f}")

                # Registrar la compra en el historial del cliente
                if "compras" not in cliente:
                    cliente["compras"] = []  # Crear lista de compras si no existe
                cliente["compras"].append({ #.append es para agregar un elemento a la lista
                    "paquete": paquete_seleccionado["nombre"],
                    "cantidad": cantidad,
                    "total": total
                })
                print("Compra registrada exitosamente.")
            else:
                print("La cantidad debe ser mayor a 0.")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Por favor, ingrese un número válido.")





# Función para elegir horario
def elegir_horario():
    horarios = ["Mañana (7:00 - 10:00)", "Tarde (11:00 - 2:00)", "Noche (3:00 - 5:00)"]
    
    i = 1
    print("Horarios disponibles:")
    for horario in horarios:
        print(f"{i}. {horario}")
        i += 1     # Incrementar el contador para mostrar el siguiente horario
    
    try:
        opcion = int(input("Elige un horario (1-3): "))
        if 1 <= opcion <= 3:     # < > <= >= == != son operadores de comparación
            print(f"Has seleccionado el horario: {horarios[opcion - 1]}")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Función para facturación
def facturacion(cliente):
    subtotal = float(input("Ingrese el subtotal de la compra:"))  # Solicitar subtotal de la compra
    descuento = float(input("Ingrese el descuento aplicado:"))  # Solicitar descuento aplicado
    iva = subtotal * 0.13  # Calcular el IVA (13% del subtotal)
    total = subtotal - descuento + iva  # Calcular el total a pagar

    print("\nFacturación:")  # Mostrar título de la factura
    print(f"Nombre del cliente: {cliente['Nombre']}")  # Mostrar nombre del cliente
    print(f"Cédula: {cliente['Cédula']}")  # Mostrar cédula del cliente
    print(f"Correo: {cliente['Correo']}")  # Mostrar correo del cliente
    print(f"Subtotal: {subtotal}")  # Mostrar subtotal
    print(f"Descuento: {descuento}")  # Mostrar descuento
    print(f"IVA: {iva}")  # Mostrar IVA
    print(f"Total a pagar: {total}")  # Mostrar total a pagar

# Flujo principal del programa
if login():  # Si el login es exitoso
    cliente = registrar_informacion()  # Registrar información del cliente
    while True:  # Bucle infinito para mostrar el menú
        opcion = menu()  # Mostrar el menú y obtener la opción seleccionada
        if opcion == "1":  # Opción 1: Ventas de paquetes
            venta_paquetes(cliente)  # Llamar a la función de venta de paquetes
        elif opcion == "2":  # Opción 2: Horarios disponibles de atención
            elegir_horario()  # Llamar a la función para elegir horario
        elif opcion == "3":  # Opción 3: Productos disponibles
            print("Opción 3 seleccionada. (Funcionalidad no implementada en este ejemplo.)")
        elif opcion == "4":  # Opción 4: Historial de compras
            print("Opción 4 seleccionada. (Funcionalidad no implementada en este ejemplo.)")
        elif opcion == "5":  # Opción 5: Facturación
            facturacion(cliente)  # Llamar a la función de facturación
            break  # Salir del bucle y terminar el programa
        else:
            print("Opción no válida. Intente nuevamente.")  # Mensaje de opción no válida