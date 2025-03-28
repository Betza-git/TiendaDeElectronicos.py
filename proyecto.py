# Definir usuarios y contraseñas en un diccionario
usuarios = {
    "usuario1": "usuario 1",  
    "usuario2": "usuario 2",
    "usuario3": "usuario 3"   
}

# Definir productos con sus precios en un diccionario
productos = {
    "1": {"nombre": "Olla Arrocera", "precio": 15000},
    "2": {"nombre": "Televisor Inteligente", "precio": 175000},
    "3": {"nombre": "Lavadora", "precio": 270000},
    "4": {"nombre": "Parlante Musical", "precio": 30000},
    "5": {"nombre": "Laptop Hp", "precio": 450000},
    "6": {"nombre": "Salir", "precio": 0},
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
    print("\nPor favor, ingrese su información para la facturación:")  # Mostrar mensaje de solicitud de información
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

# Función 1 para la venta de paquetes
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





# Función 2 para elegir horario
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


# Función 3 para productos disponibles

def disponibilidad_productos(cliente):
    while True:
        print("\nProductos disponibles:")
        for clave, valor in productos.items():
            print(f"{clave}. {valor['nombre']} - ₡{valor['precio']:,.2f}") #f"{valor['precio']:,.2f}" es para mostrar el precio con 2 decimales y separador de miles

        opcion = input("Seleccione un producto (1-6) o '0' para volver: ")

        if opcion == '0':
            break
        elif opcion == '6':
            print("Saliendo del programa...")
            return False
        elif opcion in productos:
            producto_seleccionado = productos[opcion]
            try:
                cantidad = int(input(f"Ingrese la cantidad de '{producto_seleccionado['nombre']}' que desea comprar: "))
                if cantidad > 0:   # Validar que la cantidad sea positiva
                    subtotal = producto_seleccionado["precio"] * cantidad
                    iva = subtotal * 0.13
                    total = subtotal + iva

                    print("\nResumen de la compra")
                    print(f"Producto seleccionado: {producto_seleccionado['nombre']}")
                    print(f"Cantidad: {cantidad}")
                    print(f"Precio unitario: ₡{producto_seleccionado['precio']:,.2f}")
                    print(f"Subtotal: ₡{subtotal:,.2f}")
                    print(f"IVA (13%): ₡{iva:,.2f}")
                    print(f"Total a pagar: ₡{total:,.2f}")

                    if "compras" not in cliente:    #not in es un operador de pertenencia
                        cliente["compras"] = []
                    cliente["compras"].append({
                        "producto": producto_seleccionado["nombre"],
                        "cantidad": cantidad,
                        "total": total
                    })
                else:
                    print("La cantidad debe ser mayor que 0.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")
        else:
            print("Opción no válida. Por favor seleccione 1-6.")
    return True



#Función 4 para mostrar el historial de compras
def mostrar_historial(cliente):
    if "compras" not in cliente or not cliente["compras"]:
        print("\nNo hay compras registradas en el historial.")
        return
    
    print("\n--- HISTORIAL DE COMPRAS ---")
    print(f"Cliente: {cliente['Nombre']}")
    print(f"Cédula: {cliente['Cédula']}")
    print("---------------------------------")
    
    total_general = 0
    for i, compra in enumerate(cliente["compras"], 1):
        if "paquete" in compra:  # Para compras de paquetes
            print(f"{i}. [PAQUETE] {compra['paquete']}")
        else:  # Para compras de productos individuales
            print(f"{i}. [PRODUCTO] {compra['producto']}")
        
        print(f"   Cantidad: {compra['cantidad']}")
        print(f"   Precio unitario: ₡{compra['total']/compra['cantidad']:,.3f}")
        print(f"   Total: ₡{compra['total']:,.3f}")
        print("---------------------------------")
        total_general += compra['total']
    
    print(f"TOTAL GENERAL: ₡{total_general:,.3f}")




# Función 5 para facturación
def facturacion(cliente):
    subtotal = float(input("Ingrese el subtotal de la compra:"))  # Solicitar subtotal de la compra

    descuento = subtotal - (subtotal * 0.05) 
         # Calcular descuento del 10% si el subtotal es mayor a 10000
    if subtotal > 20000:
        descuento = subtotal * 0.10
    else:
        descuento = 0
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
            disponibilidad_productos(cliente)  # Llamar a la función para productos disponibles
        elif opcion == "4":  # Opción 4: Historial de compras
            mostrar_historial(cliente)  # Llamar a la función de historial de compras
        elif opcion == "5":  # Opción 5: Facturación
            facturacion(cliente)  # Llamar a la función de facturación
            break  # Salir del bucle y terminar el programa
        else:
            print("Opción no válida. Intente nuevamente.")  # Mensaje de opción no válida