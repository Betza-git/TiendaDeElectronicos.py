# Definir usuarios y contraseñas en un diccionario
usuarios = {
    "usuario1": "usuario1",  
    "usuario2": "usuario2",
    "usuario3": "usuario3"   
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

# Mensaje de bienvenida
print("Bienvenido a la tienda de electrónicos")

# Función para validar el login del usuario
def login():                                                                   #Función para validar el login del usuario
    intentos = 3
    while intentos > 0:                                                         #Mientras haya intentos disponibles
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        if usuario in usuarios and usuarios[usuario] == contraseña:             #Verifica si el usuario y contraseña son correctos         
            print("Ingreso satisfactorio.")
            return True
        else:
            intentos -= 1                                                       #Resta un intento si el login falla                    
            print(f"Usuario o contraseña incorrectos. Le quedan {intentos} intentos.")
    print("Ha excedido el número de intentos. Saliendo de la plataforma.")
    return False

# Función para registrar información del cliente
def registrar_informacion():
    print("\nPor favor, ingrese su información para la facturación:")         #\n es un salto de línea
    print("Recuerde que la información es confidencial y no será compartida.")
    nombre = input("Ingrese su nombre completo: ")  
    cedula = input("Ingrese su cédula: ")  
    celular = input("Ingrese su número de celular: ")  
    correo = input("Ingrese su correo electrónico: ")  
    direccion = input("Ingrese su dirección: ")  
    return {
        "Nombre": nombre,
        "Cédula": cedula,
        "Celular": celular,
        "Correo": correo,
        "Dirección": direccion
    }

# Función para mostrar el menú de opciones
def menu():
    print("\nMenú de opciones:")
    print("1. Ventas de paquetes")  
    print("2. Horarios disponibles de atención")  
    print("3. Productos disponibles")  
    print("4. Historial de compras")  
    print("5. Facturación de compras")  
    opcion = input("Seleccione una opción: ")
    return opcion

# Función 1 para la venta de paquetes
def venta_paquetes(cliente):
    paquetes = {
        "1": {"nombre": "Set de componentes electrónicos", "precio": 15000},
        "2": {"nombre": "Kit de soldadura con multímetro", "precio": 21500},
        "3": {"nombre": "Set de bloques Robot Transformer", "precio": 31500}
    }

    print("\nPaquetes disponibles:")
    for clave, valor in paquetes.items():
        print(f"{clave}. {valor['nombre']} - ₡{valor['precio']:,.2f}")     # Se usa :,.2f para formatear el precio con separador de miles y 2 decimales

    try:
        opcion = input("Seleccione un paquete (1-3): ")                    # Se espera que el usuario ingrese un número entre 1 y 3
        if opcion in paquetes:
            paquete_seleccionado = paquetes[opcion]                        # Se obtiene el paquete seleccionado             
            cantidad = int(input(f"Ingrese la cantidad de '{paquete_seleccionado['nombre']}' Que desea comprar?: "))   #int convierte la entrada a un número entero
            if cantidad > 0:
                subtotal = paquete_seleccionado["precio"] * cantidad
                iva = subtotal * 0.13                                      #Calculo del IVA
                total = subtotal + iva

                print("\nResumen de la compra:")  
                print(f"Paquete seleccionado: {paquete_seleccionado['nombre']}")
                print(f"Cantidad: {cantidad}")
                print(f"Precio unitario: ₡{paquete_seleccionado['precio']:,.2f}")
                print(f"Subtotal: ₡{subtotal:,.2f}") 
                print(f"IVA (13%): ₡{iva:,.2f}")
                print(f"Total a pagar: ₡{total:,.2f}")

                if "compras" not in cliente:
                    cliente["compras"] = []
                cliente["compras"].append({                                  #.append agrega un nuevo elemento a la lista de compras
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
    
    print("Horarios disponibles:")
    for i, horario in enumerate(horarios, 1):                            #enumerate para numerar los horarios   
        print(f"{i}. {horario}")                                         #se usa {i} para mostrar el número del horario
    
    try:
        opcion = int(input("Elige un horario (1-3): "))
        if 1 <= opcion <= 3:                                             # <= y >= son operadores de comparación y se usan para verificar si la opción está dentro del rango
            print(f"Has seleccionado el horario: {horarios[opcion - 1]}")
        else:
            print("Opción inválida.")
    except ValueError:                                                 #ValueError para manejar errores de conversión de tipo
        print("Por favor, ingresa un número válido.")

# Función 3 para productos disponibles
def disponibilidad_productos(cliente):
    while True:                                                        #Este es un bucle infinito para permitir múltiples selecciones de productos         
        print("\nProductos disponibles:")
        for clave, valor in productos.items():                         #for para iterar sobre los productos
            print(f"{clave}. {valor['nombre']} - ₡{valor['precio']:,.2f}")  

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
                if cantidad > 0:
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

                    if "compras" not in cliente:
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

# Función 4 para mostrar el historial de compras               #En esta funcion se implementa if "compras" not in cliente para verificar si el cliente tiene compras registradas
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
        if "paquete" in compra:
            print(f"{i}. [PAQUETE] {compra['paquete']}")
        else:
            print(f"{i}. [PRODUCTO] {compra['producto']}")
        
        print(f"   Cantidad: {compra['cantidad']}")
        print(f"   Precio unitario: ₡{compra['total']/compra['cantidad']:,.2f}")
        print(f"   Total: ₡{compra['total']:,.2f}")
        print("---------------------------------")
        total_general += compra['total']
    
    print(f"TOTAL GENERAL: ₡{total_general:,.2f}")

# Función 5 para facturación de compras
def facturacion(cliente):
    if "compras" not in cliente or not cliente["compras"]:
        print("\nNo hay compras registradas para facturar.")
        return
    
    # Calcular subtotal sumando todas las compras
    subtotal = sum(compra['total'] / 1.13 for compra in cliente["compras"])  # Excluyendo IVA
   
    
    # Calcular descuento 10% si subtotal > 20000
    if subtotal > 20000:
        descuento = subtotal * 0.10
    else:
        descuento = 0
    
    # Calcular IVA 13% del subtotal
    iva = subtotal * 0.13
    
    # Calcular total
    total = subtotal - descuento + iva
    
    # Mostrar factura detallada
    print("\n" + "="*50)
    print("FACTURA ELECTRÓNICA".center(50))  #  .center(50) centra el texto
    print("="*50)                            #**50) centra el texto
    print(f"Cliente: {cliente['Nombre']}")
    print(f"Cédula: {cliente['Cédula']}")
    print(f"Correo: {cliente['Correo']}")
    print("-"*50)
    
    print("\nDetalle de productos:")
    for compra in cliente["compras"]:          #Se asume que cada compra tiene un producto o paquete
        if "paquete" in compra:
            print(f"[PAQUETE] {compra['paquete']:30} {compra['cantidad']:2} x ₡{compra['total']/compra['cantidad']/1.13:,.2f}")   #Esta linea es para mostrar el precio unitario sin IVA
        else:
            print(f"[PRODUCTO] {compra['producto']:28} {compra['cantidad']:2} x ₡{compra['total']/compra['cantidad']/1.13:,.2f}")
    
    print("\n" + "-"*50)                                   # Separa el detalle de la factura
    print(f"SUBTOTAL: ₡{subtotal:>37,.2f}")
    print(f"DESCUENTO ({'10%' if descuento > 0 else '0%'}): ₡{descuento:>30,.2f}")    # Se muestra el descuento si aplica
    print(f"IVA (13%): ₡{iva:>35,.2f}")                                               # Calculo del IVA 
    print("="*50)
    print(f"TOTAL A PAGAR: ₡{total:>32,.2f}")                                            # Total a pagar
    print("="*50)

# Flujo principal del programa
if login():
    cliente = registrar_informacion()                        # Registra la información del cliente
    while True:                                              # Usamos while True para mantener el menú activo
        opcion = menu()
        if opcion == "1":
            venta_paquetes(cliente)                          # Llama a la función de venta de paquetes  
        elif opcion == "2":                                  # Llama a la función de elegir horario
            elegir_horario()
        elif opcion == "3":
            disponibilidad_productos(cliente)                # Llama a la función de disponibilidad de productos       
        elif opcion == "4":
            mostrar_historial(cliente)                       # Llama a la función de mostrar historial de compras                           
        elif opcion == "5":
            facturacion(cliente)                             # Llama a la función de facturación de compras
        elif opcion == "6":
            print("Saliendo del menú. Gracias por usar el sistema.")
            break                                           # Se usa break para salir del bucle y terminar el programa
        else:
            print("Opción no válida. Intente nuevamente.")