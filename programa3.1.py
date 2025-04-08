def crear_cliente(NIF: str, direccion: str, telefono: str, correo: str, preferente: bool):
    nuevo_cliente = {
        'NIF': NIF,
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
        print(f"Dirección: {cliente['direccion']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Correo: {cliente['correo']}")
        print(f"Cliente preferente: {'Si' if cliente['preferente'] else 'No'}")
    else:
        print(f"No existe un cliente con NIF {NIF}")

def listar_clientes(base_de_datos: dict) -> None:
    print("Lista de clientes:")
    for NIF, cliente in base_de_datos.items():
        print(f"NIF: {NIF}, Correo: {cliente['correo']}, {'Cliente preferente' if cliente['preferente'] else 'Cliente normal'}")

def listar_clientes_preferentes(base_de_datos: dict) -> None:
    print("Lista de clientes preferentes:")
    for NIF, cliente in base_de_datos.items():
        if cliente['preferente']:
            print(f"NIF: {NIF}, Correo: {cliente['correo']}")

def main():
    clientes = {}
    
    mi_cliente1 = crear_cliente('RUBM0317263', 'calle mision, sauzal', '615212162', 'mariana@gmail.com', True)
    clientes = agregar_cliente(clientes, mi_cliente1)

    mi_cliente2 = crear_cliente('54321678X', 'Avenida Principal 123', '678901234', 'ana@gmail.com', False)
    mi_cliente3 = crear_cliente('87654321Y', 'Calle Secundaria 45', '612345678', 'carlos@gmail.com', True)
    
    clientes = agregar_cliente(clientes, mi_cliente2)
    clientes = agregar_cliente(clientes, mi_cliente3)
    
    listar_clientes(clientes)
    
    mostrar_cliente(clientes, 'RUBM0317263')
    
    listar_clientes_preferentes(clientes)
    
    clientes = eliminar_cliente(clientes, '54321678X')
    
    listar_clientes(clientes)

if __name__ == '__main__':
    main()