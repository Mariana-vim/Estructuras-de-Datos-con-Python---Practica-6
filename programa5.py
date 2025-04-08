def crear_cliente(NIF: str, nombre: str, direccion: str, telefono: str, correo: str, preferente: bool):
    nuevo_cliente = {
        'NIF': NIF,
        'nombre': nombre,
        'direccion': direccion,
        'telefono': telefono,
        'correo': correo,
        'preferente': preferente
    }

    return nuevo_cliente

def agregar_cliente(base_de_datos: dict, cliente: dict) -> dict:
    base_de_datos[cliente['NIF']] = cliente

    return base_de_datos

def eliminar_cliente(base_de_datos: dict, NIF: str) -> dict:
    if NIF in base_de_datos:
        del base_de_datos[NIF]
    
    return base_de_datos

def mostrar_cliente(base_datos: dict, NIF: str) -> None:
    if NIF in base_datos:
        cliente = base_datos[NIF]
        print(f"NIF: {cliente['NIF']}")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Direccion: {cliente['direccion']}")
        print(f"Telefono: {cliente['telefono']}")
        print(f"Correo: {cliente['correo']}")
        print(f"Cliente preferente: {'Si' if cliente['preferente'] else 'No'}")
    else:
        print(f"No existe un cliente con NIF {NIF}")

def listar_clientes(base_de_datos: dict) -> None:
    if not base_de_datos:
        print("No hay clientes en la base de datos.")
        return
        
    print("Lista de todos los clientes:")
    for NIF, cliente in base_de_datos.items():
        print(f"NIF: {NIF}, Nombre: {cliente['nombre']}")

def listar_clientes_preferentes(base_de_datos: dict) -> None:
    preferentes_encontrados = False
    
    print("Lista de clientes preferentes:")
    for NIF, cliente in base_de_datos.items():
        if cliente['preferente']:
            print(f"NIF: {NIF}, Nombre: {cliente['nombre']}")
            preferentes_encontrados = True
    
    if not preferentes_encontrados:
        print("No hay clientes preferentes en la base de datos.")

def mostrar_menu():
    print("\nGESTION DE CLIENTES")
    print("1. Anadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")

def main():
    clientes = {}
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Selecciona una opcion (1-6): "))
        except ValueError:
            print("Error!! Introduce un numero entre 1 y 6")
            continue
        
        if opcion == 1:
            print("\nAnadir nuevo cliente")
            nif = input("Introduce el NIF del cliente: ")
            nombre = input("Introduce el nombre del cliente: ")
            direccion = input("Introduce la direccion del cliente: ")
            telefono = input("Introduce el telefono del cliente: ")
            correo = input("Introduce el correo del cliente: ")
            
            preferente_input = input("Es un cliente preferente? (s/n): ").lower()
            preferente = preferente_input == 's' or preferente_input == 'si'
            
            nuevo_cliente = crear_cliente(nif, nombre, direccion, telefono, correo, preferente)
            clientes = agregar_cliente(clientes, nuevo_cliente)
            print(f"Cliente {nombre} con NIF {nif} ha sido anadido")
            
        elif opcion == 2:
            print("\nEliminar cliente")
            nif = input("Introduce el NIF del cliente a eliminar: ")
            if nif in clientes:
                nombre = clientes[nif]['nombre']
                clientes = eliminar_cliente(clientes, nif)
                print(f"Cliente {nombre} con NIF {nif} ha sido eliminado")
            else:
                print(f"No existe un cliente con NIF {nif}")
                
        elif opcion == 3:
            print("\nMostrar datos de cliente")
            nif = input("Introduce el NIF del cliente a mostrar: ")
            mostrar_cliente(clientes, nif)
            
        elif opcion == 4:
            print("\nLista de todos los clientes")
            listar_clientes(clientes)
            
        elif opcion == 5:
            print("\nLista de solo clientes preferentes")
            listar_clientes_preferentes(clientes)
            
        elif opcion == 6:
            print("\nGracias por utilizar el programa de gestion de clientes.")
            break
            
        else:
            print("Opcion no valida, introduce un numero entre 1 y 6.")

if __name__ == '__main__':
    main()