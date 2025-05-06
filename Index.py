import Funciones 
import Controlador

Funciones.cls()
Funciones.inicio()
print()

def main():
    print("Ingresa tu usuario para iniciar sesión:")
    usuario = Controlador.login()
    if usuario:
        print(f"Hola {usuario} =)")
        Funciones.pausaT(2)
        Funciones.cls()
        Funciones.bienvenida()
    else:
        print("No se pudo iniciar sesión. Saliendo del sistema...")
        Funciones.pausaT(4)
        Funciones.cls()
        Controlador.login()
        print()

    cliente = Controlador.registrar_informacion()
    Funciones.msg("Información registrada correctamente.")
    while True:
        print("\n¿Deseas editar la información registrada?") 
        respuesta = input("\nPor favor, ingresa 's' para sí o 'n' para no: ").strip().lower()
        if respuesta in ('s', 'n'):
         break   
    if respuesta == 's':
        cliente = Controlador.editar_informacion()  
        Funciones.msg("\nInformación editada correctamente.")
        Funciones.pausaT(2)
        Funciones.cls()   
    elif respuesta == 'n':
        Funciones.pausaT(2)
        Funciones.cls()
    else: 
        Funciones.pausaT(3)
        Funciones.cls()   

    while True:
        opcion = Controlador.menu()
        if opcion == "1":
            Controlador.venta_paquetes(cliente)
            Funciones.pausaT(4)
            Funciones.cls()            
        elif opcion == "2":
            Controlador.elegir_horario()
            Funciones.pausaT(3)
            Funciones.cls()  
        elif opcion == "3":
            Controlador.disponibilidad_productos(cliente)  
        elif opcion == "4":
            Controlador.mostrar_historial(cliente)  
        elif opcion == "5":
            Controlador.facturacion(cliente) 
        elif opcion == "6":
            Controlador.salir()   
        else:
            print("Opción inválida.")
            break

if __name__ == "__main__":
    main()
