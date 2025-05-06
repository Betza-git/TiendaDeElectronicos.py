import Funciones
  
def login(): 
    """Función para iniciar sesión
        Se condicionan los intentos de acceso """
    usuarios = [["admin", "admin"], ["admin2", "admin2"], ["admin3", "admin3"]]
    intentos = 3
    while intentos > 0:
        username = input("Usuario: ")
        password = input("Contraseña: ")
        for u in usuarios:
            if username == u[0] and password == u[1]:
                return username
        intentos -= 1
        print(f"Error. Intentos restantes: {intentos}")
    print("Demasiados intentos fallidos.")
    return None



def registrar_informacion():
    """Función para registrar la información"""
    print("\n--- Registro de datos para la facturación ---")
    print("Recuerda que la información será confidencial.")
    nombre = input("Nombre: ")
    cedula = input("Cédula: ")
    celular = input("Celular: ")
    correo = input("Correo: ")
    direccion = input("Dirección: ")
    return [nombre , cedula, celular, correo, direccion, []]  

def editar_informacion():
    """Edicion de los datos en caso de que el usuario lo requiera"""
    print("\n--- Editar información ---")
    nombre = input("Nombre: ")
    cedula = input("Cédula: ")
    celular = input("Celular: ")
    correo = input("Correo: ")
    direccion = input("Dirección: ")
    return [nombre, cedula, celular, correo, direccion, []]


def menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Venta de paquetes")
    print("2. Horarios disponibles")
    print("3. Productos disponibles")
    print("4. Historial de compras")
    print("5. Facturación")
    print("6. Salir")
    return input("Opción: ")


def venta_paquetes(cliente):
    paquetes = [
        ["1", "Set de componentes electrónicos", 15000],
        ["2", "Kit de soldadura con multímetro", 21500],
        ["3", "Set de bloques Robot Transformer", 31500],
        ["4", "Kit de robótica básica", 45000],
        ["5", "Kit de robótica avanzada", 65000] 
    ]

    print("\n--- Paquetes disponibles ---")
    for p in paquetes:
        print(f"{p[0]}. {p[1]} - ₡{p[2]:,.2f}")
    opcion = input("Seleccione un paquete: ")
    seleccionado = None
    for p in paquetes:
        if p[0] == opcion:
            seleccionado = p
            break

    if seleccionado:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad > 0:
                subtotal = cantidad * seleccionado[2]
                iva = subtotal * 0.13
                total = subtotal + iva
                cliente[5].append(["paquete", seleccionado[1], cantidad, total])
                print(f"Total con IVA: ₡{total:,.2f}")
            else:
                print("Cantidad debe ser mayor a 0.")
        except ValueError:
            print("Entrada inválida.")
    else:
        print("Opción no válida.")


def elegir_horario():
    horarios = ["Mañana (7-10)", "Tarde (1-3)", "Noche (3-5)"]
    print("\n--- Horarios de atención ---")
    for i in range(len(horarios)):
        print(f"{i+1}. {horarios[i]}")
    try:
        opcion = int(input("Elija horario (1-3): "))
        if 1 <= opcion <= 3:
            print(f"Seleccionado: {horarios[opcion - 1]}")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Debe ingresar un número.")

def disponibilidad_productos(cliente):
    productos = [
        ["1", "Olla Arrocera", 15000],
        ["2", "Televisor", 175000],
        ["3", "Lavadora", 270000],
        ["4", "Parlante", 30000],
        ["5", "Laptop", 450000]
    ]
    print("\n--- Productos disponibles ---")
    for p in productos:
        print(f"{p[0]}. {p[1]} - ₡{p[2]:,.2f}")
    opcion = input("Seleccione producto: ")
    seleccionado = None
    for p in productos:
        if p[0] == opcion:
            seleccionado = p
            break
    if seleccionado:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad > 0:
                subtotal = cantidad * seleccionado[2]
                iva = subtotal * 0.13
                total = subtotal + iva
                cliente[5].append(["producto", seleccionado[1], cantidad, total])
                print(f"Total con IVA: ₡{total:,.2f}")
            else:
                print("Cantidad debe ser mayor que 0.")
        except ValueError:
            print("Debe ingresar un número.")
    else:
        print("Opción inválida.")


def mostrar_historial(cliente):
    print("\n--- Historial de compras ---")
    if not cliente[5]:
        print("No hay compras.")
        return

    total = 0
    for i in range(len(cliente[5])):
        compra = cliente[5][i]
        print(f"{i+1}. [{compra[0]}] {compra[1]} x{compra[2]} - ₡{compra[3]:,.2f}")
        total += compra[3]
        print(f"\nTOTAL GENERAL: ₡{total:,.2f}")
  
  
def facturacion(cliente):
    print("************************************")
    print("  ----- Factura Electrónica ------  ")
    print("************************************")
    print()
    if not cliente[5]:
        print("No hay compras para facturar.")
        return

    subtotal = 0
    for compra in cliente[5]:
        subtotal += compra[3] / 1.13

    descuento = 0
    if subtotal > 20000:
        descuento = subtotal * 0.10

    iva = subtotal * 0.13
    total = subtotal - descuento + iva
    
    
    print(f"Cliente: {cliente[0]}")
    print(f"Cédula: {cliente[1]}")
    print("____________________________________________________")
    print("\nDetalle de compras:")
    for compra in cliente[5]:
        print(f"{compra[1]} x{compra[2]} - ₡{compra[3]:,.2f}")
    print("\nSubtotal: ₡{0:,.2f}".format(subtotal))
    print("Descuento: ₡{0:,.2f}".format(descuento))
    print("IVA (13%): ₡{0:,.2f}".format(iva))
    print("TOTAL A PAGAR: ₡{0:,.2f}".format(total))
    print("____________________________________________________")

def salir():
    print("Gracias por visitar nuestra tienda.")
    print("¡Hasta luego!")
    Funciones.pausaT(3)
    Funciones.cls() 
       
